from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import pymongo
import uuid
import subprocess
import os

@api_view(['PUT'])
def put_report(request, token, **kwargs):

    '''
    'id': '7001',
    'roomId': '101',
    'text': 'string'
    '''
    # TODO: token from where?
    required_keys = ['candidate_id', 'text', 'token']

    report_data = request.data
    token = report_data['token']

    # Check key error

    if set(required_keys) != set(report_data):
        return Response(
            {
                'status': '30',
                'error': 'Key error'
            },
            status.HTTP_400_BAD_REQUEST
        )

    client = pymongo.MongoClient()
    db = client[settings.DB_NAME]

    # Check user permission

    access_denied = False
    applicant = db.users.find({'token': token})
    if applicant.count() == 0:
        access_denied = True
    else:
        for item in applicant:
            if item['type'] not in ['hr', 'interviewer']:
                access_denied = True
                break
    if access_denied:
        return Response(
            {
                'status': '30',
                'error': 'Permission denied.'
            },
            status.HTTP_403_FORBIDDEN
        )

    # Set path record
    # TODO: Should there be more than one report for each candidate?

    report_id = str(uuid.uuid4())
    while db.report.find({'report_id': report_id}).count() > 0:
        report_id = str(uuid.uuid4())
    report_path =  os.path.join(settings.REPORT_PATH, report_id)
    tex_file_path = os.path.join(settings.TEX_PATH, report_id)
    db.report.insert_one(
        {
            'candidate_id': report_data['candidate_id'],
            'report_id': report_id,
            'path': report_path + '.pdf'
        }
    )
    db.candidate.update({'id': report_data['candidate_id']}, {$set: {report_id}})

    # Get related data from 3 collections
    candidate_user_data = db.users.find_one({'candidate_id': report_data['candidate_id']})
    candidate_candidate_data = db.candidate.find_one({'id': report_data['candidate_id']})

    candidate_name = candidate_candidate_data['name']
    candidate_id = report_data['candidate_id']
    candidate_organization = candidate_user_data['organization']
    candidate_contact = candidate_user_data['contact']
    candidate_phone = candidate_candidate_data['phone']
    candidate_email = candidate_candidate_data['email']
    candidate_status = candidate_candidate_data['status']

    candidate_video = candidate_candidate_data['record']['video']
    candidate_board = candidate_candidate_data['record']['board']
    candidate_chat = candidate_candidate_data['record']['chat']
    candidate_code = candidate_candidate_data['record']['code']

    room_id = candidate_candidate_data['roomId']
    room_data = db.room.find_one({'id': room_id})
    interviewer_name = room_data['interviewer']

    # TODO: Where is the logo? room_data['logo'] returns what?
    logo = "./generate_report/iitmlogo.pdf"


    # Write report

    lines = []
    with open(settings.REPORT_PATH + 'header.tex', 'r') as fheader:
            # Warning: Dirty implementations
        lines.append(fheader.read())
        lines.append("\\begin{document}")
        lines.append("\\begin{tabular*}{7in}{l@{\extracolsep{\\fill}}r}")
        lines.append(" & \\multirow{4}{*}{\includegraphics[scale=0.19]{" + logo + "}} \\\\")
        lines.append(" & \\\\")
        lines.append("\\textbf{\Large " + candidate_name + "$|$" + candidate_id + "} & \\\\")
        lines.append(candidate_organization + "& \\\\")
        lines.append(candidate_phone + "& \\\\")
        lines.append(candidate_email + "& \\\\")
        lines.append(candidate_contact + \\\\)
        lines.append("\\end{tabular*} \\\\")

        lines.append("\\reshading{\Large{面试结果：" + candidate_status + "}}")
        lines.append("\\rule[3pt]{17.8cm}{0.05em}")
        lines.append("\\reshading{HR 与面试官信息}")
        lines.append("\\begin{itemize}")
        lines.append("\\item")
        lines.append("    \\ressubheading{HR}{}{HR\\_name}{HR\\_email}")
        lines.append("\\item")
        lines.append("    \\ressubheading{面试官}{}{" + interviewer_name + "}{Interviewer\\_email}")
        lines.append("\\end{itemize}")

        lines.append("\\reshading{面试记录与面试官评价}")
        lines.append("    \\begin{center}")
        lines.append("    \\parbox{6.762in}{" + report_data['text'] + "}")
        lines.append("\\end{center}")

        lines.append("\\reshading{面试题记录（文字部分）}")
        lines.append("\\begin{itemize}")
        lines.append("\\item")
        # TODO: Question format
        # lines.append("    \\ressubheading{选择题}{}{Passed}{}")
        # lines.append("    \\begin{itemize}")
        # lines.append("        \\resitem{title1}")
        # lines.append("    \\end{itemize}")

        lines.append("\\reshading{面试题记录（视频与音频部分）}")
        lines.append("\\begin{itemize}")
        lines.append("\\item")
        lines.append("    白板记录")
        lines.append("    \\begin{itemize}")
        lines.append("        \\resitem{\\bf File} " + candidate_board + "}")
        lines.append("    \\end{itemize}")
        lines.append("\\item")
        lines.append("    视频文件")
        lines.append("    \\begin{itemize}")
        lines.append("        \\resitem{\\bf File} " + candidate_video + "}")
        lines.append("\\end{itemize}")

        lines.append("\\end{document}")

    with open(report_path + ".tex", 'w') as f:
        f.writelines(lines)

    subprocess.call('xelatex ' + report_path + '.tex -output-directory=' + settings.REPORT_PATH)

    return Response(
        {
            'id': report_id,
            'roomId': report_data['candidate_id'],
            'text': report_data['text']
        }
    )



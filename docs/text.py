from blacksheep.server.openapi.common import (
    ContentInfo,
    EndpointDocs,
    HeaderInfo,
    RequestBodyInfo,
    ResponseExample,
    ResponseInfo,
)
from domain.text import TextClassifier, Type_of_df

# create_token = EndpointDocs(
#     summary="Add a new token into a group chat",
#     request_body=RequestBodyInfo(
#         examples={
#             "v1": TextClassifier(
#                 token_address="Yeah he got in at 2 and was v apologetic."
#             ),
#         },
#     ),
#     responses={
#         200: ResponseInfo(
#             "Successfully add a new token into a group chat",
#             content=[
#                 ContentInfo(
#                     Token,
#                     examples=[
#                         ResponseExample(
#                             {
#                                 'message': "Pair Added"
#                             }
#                         )
#                     ],
#                 )
#             ],
#         ),
#         400: "Pair Already Added",
#         422: "Please input valid Token Address!"
#     },
# )
Text = EndpointDocs(
    summary="Update token notification",
    request_body=RequestBodyInfo(
        examples={
            "v1": TextClassifier(
                Text='Yeah he got in at 2 and was v apologetic.',
                is_paused=True
            ),
        },
    ),
    responses={
        200: ResponseInfo(
            "Successfully pausing / resuming token notification",
            content=[
                ContentInfo(
                    Text,
                    examples=[
                        ResponseExample(
                            {
                                'message': "Token buy notification successfully paused!"
                            }
                        )
                    ],
                )
            ],
        ),
    },
)
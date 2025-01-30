from rest_framework.views import APIView
from rest_framework.response import Response

from apps.api.slack.services.slack_manager import SlackManager


class SlackView(APIView):
    def post(self, request, *args, **kwargs):
        text = request.data.get("text")
        block = request.data.get("block")
        attachments = request.data.get("attachments")
        thread_ts = request.data.get("thread_ts")

        channel = ""
        token = ""

        slack_manager = SlackManager(channel, token)
        new_thread_ts = slack_manager.post_message(
            text=text, blocks=block, attachments=attachments, thread_ts=thread_ts
        )

        if new_thread_ts:
            return Response({"thread_ts": new_thread_ts}, status=200)
        else:
            return Response({"message": "Slack message sent"}, status=500)

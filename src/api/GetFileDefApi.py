from base.UseApi import UseApi
from protocol.Factory import Factory

class GetFileDefApi(UseApi):

    def parameter_check(self):
        """
        パラメータチェック
        """
        print("パラメータチェックを実行します")

    def create_response(self):
        """
        レスポンス構築
        """
        print("レスポンスを作成します")

    def custom_execute(self):
        """
        レスポンス構築
        """
        print("処理を実行します")
        protocol = Factory.get_protocol()
        protocol.get_connection_def()

api = GetFileDefApi()
api.execute()

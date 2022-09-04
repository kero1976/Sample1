from base.Protocol import Protocol

class JX(Protocol):

    def get_connection_def(self):
        print("JX接続定義を取得します")
    
    def get_file_def(self):
        print("JXファイル定義を取得します")

    def get_transaction(self):
        print("JXトランザクションを取得します")
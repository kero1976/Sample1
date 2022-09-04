import abc


class UseApi(metaclass=abc.ABCMeta):
    """
    運用APIベースクラス
    最初にパラメータチェックを行い、色々処理を行い、最後にレスポンスを返す
    """

    @abc.abstractmethod
    def parameter_check(self):
        """
        パラメータチェック
        """

    @abc.abstractmethod
    def create_response(self):
        """
        レスポンス構築
        """

    @abc.abstractmethod
    def custom_execute(self):
        """
        色々な処理
        """

    def execute(self):
        self.parameter_check()
        self.custom_execute()
        self.create_response()

import abc


class Protocol(metaclass=abc.ABCMeta):
    """
    プロトコルベースクラス
    """

    @abc.abstractmethod
    def get_connection_def(self):
        """
        接続定義取得
        """

    @abc.abstractmethod
    def get_file_def(self):
        """
        ファイル定義取得
        """

    @abc.abstractmethod
    def get_transaction(self):
        """
        トランザクション取得
        """
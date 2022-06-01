
"""

    The Dependency inversion Principle (DIP)

	    "classes should depend upon abstractions, not concretions"

"""

from enum import Enum

class Dependency(Enum):
  LANGUAGE_CODE = "Python"
  FRAMEWORK_CODE = "Django"


class AbstractClass(ABC):

    def get_channel_message(self) -> str:
        print("--------------------AbstractClass---------")
      

class AbstractCommunicator(ABC):

    def get_channel(self) -> AbstractClass:
        pass




    # @final
    # def communicate(self, conversation: AbstractConversation):
    #     print(*conversation.do_conversation(),
    #           self.get_channel().get_channel_message(),
    #           sep = '\n')



"""
Active Directory
"""
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user == group.get_name():
        return True
    if user in group.get_users():
        return True
    for i in group.get_groups():
        return is_user_in_group(user, i)
    return False

parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

#Test Case 1
print("Test Case 1 - ")
print(is_user_in_group("parent", child)) # False

#Test Case 2
print("Test Case 1 - ")
print(is_user_in_group("sub_child_user", parent)) # True

#Test Case 3
print("Test Case 1 - ")
print(is_user_in_group("child", parent)) # True

#Test Case 4
print("Test Case 1 - ")
print(is_user_in_group("", child)) # False

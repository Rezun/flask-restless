from blinker import Signal


class PreProcessors:
    def __init__(self):
        self.get_collection = Signal()
        self.get_resource = Signal()
        self.get_relation = Signal()
        self.get_related_resource = Signal()
        self.delete_resource = Signal()
        self.post_resource = Signal()
        self.patch_resource = Signal()
        self.get_relationship = Signal()
        self.delete_relationship = Signal()
        self.post_relationship = Signal()
        self.patch_relationship = Signal()


class PostProcessors:
    def __init__(self):
        self.get_collection = Signal()
        self.get_resource = Signal()
        self.get_to_many_relation = Signal()
        self.get_to_one_relation = Signal()
        self.get_related_resource = Signal()
        self.delete_resource = Signal()
        self.post_resource = Signal()
        self.patch_resource = Signal()
        self.get_to_many_relationship = Signal()
        self.get_to_one_relationship = Signal()
        self.delete_relationship = Signal()
        self.post_relationship = Signal()
        self.patch_relationship = Signal()


class InsteadOfProcessors:
    pass

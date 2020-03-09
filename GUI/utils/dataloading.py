class SensorsDataset():
    """
    Our custom Dataset, for preparing ...
        - __getitem__(self, index): we have to return the properly
            processed data-item from our dataset with a given index
    """

    def __init__(self, x, y):
        """
        In the initialization of the dataset we will have to assign the
        input values to the corresponding class attributes
        and preprocess the samples

        Args:
            x (list): 
            y (list): 
        """
        pass

    def __len__(self):
        """
        Returns the length of the dataset.

        Returns:
            (int): the length of the dataset
        """

        return len(self.data)

    def __getitem__(self, index):
        """
        Returns the _transformed_ item from the dataset

        Args:
            index (int):

        Returns:
            (tuple):
                * res (ndarray): 
                * length (int): the length of the res
        """

        pass
from typing import Dict, Union, Iterator

import torch

from srl_bert.common.registrable import Registrable
from srl_bert.data.instance import Instance
from srl_bert.data.vocabulary import Vocabulary


TensorDict = Dict[str, Union[torch.Tensor, Dict[str, torch.Tensor]]]
"""
`TensorDict` is the type we use for batches.
"""


class DataLoader(Registrable):
    """
    A `DataLoader` is responsible for generating batches of instances from a
    [`DatasetReader`](/api/data/dataset_readers/dataset_reader/#datasetreader),
    or another source of data.

    This is purely an abstract base class. All concrete subclasses must provide
    implementations of the following methods:

      - [`__iter__()`](#__iter__) that creates an iterable of `TensorDict`s,
      - [`iter_instances()`](#iter_instances) that creates an iterable of `Instance`s,
      - [`index_with()`](#index_with) that should index the data with a vocabulary, and
      - [`set_target_device()`](#set_target_device), which updates the device that batch
        tensors should be put it when they are generated in `__iter__()`.

    Additionally, this class should also implement `__len__()` when possible.

    The default implementation is
    [`MultiProcessDataLoader`](../multiprocess_data_loader/#multiprocessdataloader).
    """

    default_implementation = "multiprocess"

    def __len__(self) -> int:
        raise TypeError

    def __iter__(self) -> Iterator[TensorDict]:
        raise NotImplementedError

    def iter_instances(self) -> Iterator[Instance]:
        raise NotImplementedError

    def index_with(self, vocab: Vocabulary) -> None:
        raise NotImplementedError

    def set_target_device(self, device: torch.device) -> None:
        raise NotImplementedError

#!/usr/bin/env python3
"""Task 0"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Calculate the start and end index for the pagination parameters.

    Returns:
        tuple: A tuple containing the start index and the end index.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)

# Definition for singly-linked list.
#
defmodule ListNode do
  @type t :: %__MODULE__{
          val: integer,
          next: ListNode.t() | nil
        }
  defstruct val: 0, next: nil
end

defmodule Solution do
  test1 = %ListNode{val: 1, next: %ListNode{val: 2, next: %ListNode{val: 3}}}
  test2 = %ListNode{val: 3, next: %ListNode{val: 4, next: %ListNode{val: 6}}}
  @spec add_two_numbers(l1 :: ListNode.t | nil, l2 :: ListNode.t | nil) :: ListNode.t | nil
  def add_two_numbers(l1, l2) do
    "Test!"
  end
  def test_two_numvers() do
    add_two_numbers(test1,test2)
  end
end

Solution.test_two_numbers()

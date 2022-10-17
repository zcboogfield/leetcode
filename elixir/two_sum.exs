defmodule Solution do
  @moduledoc """
    Not too bad for the first run, speed was okay but mem usage was atrocious.
    Right now we're at O(1<n<2)
    Is there possibly a way to not need the indexing?

    The big takeway is that we most likely want to look at IO.inspects vs IO.puts.
    I think mostly that it is IO.puts only takes a string while inspects is a bit more nuanced.
  """
  @spec two_sum(nums :: [integer], target :: integer) :: [integer]
  def two_sum(nums, target) do
    Enum.reduce_while(Enum.with_index(nums), %{}, fn tup, acc -> 
      if Map.has_key?(acc, target-elem(tup,0)),
        do: {:halt, [acc[target-elem(tup,0)], elem(tup,1)]}, 
        else: {:cont, Map.put(acc, elem(tup,0), elem(tup,1)) }      
      end)
  end
end

IO.inspect(Solution.two_sum([2,7,11,15], 9))

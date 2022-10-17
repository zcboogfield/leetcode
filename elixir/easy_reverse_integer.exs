defmodule Solution do
  @spec reverse(x :: integer) :: integer
  def reverse(x) do
    abs(x)
    |> Integer.to_string() 
    |> String.reverse()
    |> String.to_integer()
    |> (&(if x < 0, do: -&1, else: &1)).()
    |> (&(if &1 < -Integer.pow(2,31) || &1 > Integer.pow(2,31) - 1, do: 0, else: &1)).() 
  end
end

IO.inspect(Solution.reverse(-23))


using System.Collections;

namespace Sort
{
    public class ReverseInsertionSort : ISort
    {
        public ArrayList Sort(ArrayList inArray)
        {
            for (int i = 0; i < inArray.Count; i++)
            {
                var current = (int)inArray[i];
                int j = i - 1;

                while (j > -1 && (int)inArray[j] < current)
                {
                    inArray[j + 1] = inArray[j];
                    j--;
                }
                inArray[j + 1] = current;
            }
            return inArray;
        }
    }
}
using System.Collections;

namespace Sort
{
    public class SelectionSort : ISort
    {
        public ArrayList Sort(ArrayList inArray)
        {
            for (int i = 0; i < inArray.Count; i++)
            {
                var min = inArray[i];
                int j = i + 1;
                while( j < inArray.Count)
                {
                    if((int)inArray[j] < (int)min)
                    {
                        min = inArray[j];
                        inArray[j] = inArray[i];
                        inArray[i] = min;

                    }
                    j++;
                }
            }
            return inArray;
        }
    }
}

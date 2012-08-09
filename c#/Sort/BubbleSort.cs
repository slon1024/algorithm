using System.Collections;

namespace Sort
{
    public class BubbleSort : ISort
    {
        public ArrayList Sort(ArrayList inArray)
        {
            for (int i = 0; i < inArray.Count; i++)
            {
                for (int j = i; j < inArray.Count; j++)
                {
                    if ((int)inArray[j] < (int)inArray[i])
                    {
                        var tmp = inArray[i];
                        inArray[i] = inArray[j];
                        inArray[j] = tmp;
                    }
                }
            }

            return inArray;
        }
    }
}

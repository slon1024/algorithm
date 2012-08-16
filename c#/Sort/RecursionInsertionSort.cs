using System.Collections;

namespace Sort
{
    public class RecursionInsertionSort : ISort
    {
        public ArrayList Sort(ArrayList inArray)
        {
            if (inArray.Count < 2)
                return inArray;
            
            int index = inArray.Count - 1;
            var last = (int)inArray[index];
            inArray.RemoveAt(index);
            ArrayList rest = Sort(inArray);

            return Merge(rest, last);
        }

        public ArrayList Merge(ArrayList rest, int last)
        {
            for (int i = 0; i < rest.Count; i++ )
            {
                if ((int)rest[i] > last)
                {
                    rest.Insert(i, last);
                    return rest;
                }
            }

            rest.Add(last);
            return rest;
        }
    }
}


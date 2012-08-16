using System.Collections;
using System.Collections.Generic;

namespace Sort
{
    public class QuickSort : ISort
    {

        private int _pivot = 0;
        public int PivotIndex
        {
            get { return _pivot; }
            set { _pivot = value >> 1; }
        }

        public ArrayList Sort(ArrayList inArray)
        {
            if (inArray.Count < 2)
                return inArray;

            PivotIndex = inArray.Count;
            var pivot = inArray[PivotIndex];
            inArray.RemoveAt(PivotIndex);
            
            ArrayList less = new ArrayList(), greater = new ArrayList();
            for (int i = 0; i < inArray.Count; i++ )
            {
                if ((int)inArray[i] < (int)pivot)
                    less.Add(inArray[i]);
                else
                    greater.Add(inArray[i]);
            }

            ArrayList result = Sort(less);
            result.Add(pivot);
            result.AddRange(Sort(greater));

            return result;
        }
    }
}

using System.Collections;

namespace Sort
{
    public class MergeSort : ISort
    {
        public ArrayList Sort(ArrayList inArray)
        {
            if (1 == inArray.Count)
                return inArray;

            int middle = inArray.Count >> 1;
            ArrayList left = Sort(inArray.GetRange(0, middle));
            ArrayList right = Sort(inArray.GetRange(middle, inArray.Count - middle));
            return Merge(left, right);
            
        }

        public static ArrayList Merge(ArrayList left, ArrayList right)
        {
            var result = new ArrayList();
            int leftptr=0, rightptr=0;
            
            while (leftptr < left.Count && rightptr < right.Count)
                result.Add((int) left[leftptr] < (int) right[rightptr] ? left[leftptr++] : right[rightptr++]);

            if (leftptr < left.Count)
                result.AddRange(left.GetRange(leftptr, left.Count - leftptr));

            if (rightptr < right.Count)
                result.AddRange(right.GetRange(rightptr, right.Count - rightptr));

            return result;
        }
    }
}
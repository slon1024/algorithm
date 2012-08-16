using System.Collections;


namespace Sort
{
    public class HeapSort : ISort
    {

        private ArrayList _inArray;

        public ArrayList Sort(ArrayList inArray)
        {
            
            if (inArray.Count < 2)
                return inArray;

            _inArray = inArray;
            int start = (_inArray.Count - 2) >> 1;
            int end = _inArray.Count - 1;

            while (start > -1)
            {
                ShiftDown(start, _inArray.Count - 1);
                start--;
            }
            
            while(end > 0)
            {
                if((int)_inArray[end] < (int)_inArray[0])
                    Swap(end,0);

                end--;

                ShiftDown(0, end);
            }

            return _inArray;
        }



        private void ShiftDown(int start, int end)
        {
            int root = start;
            while(root*2+1 <= end)
            {
                int child = root*2 + 1, swap = root;
                
                if((int)_inArray[swap] < (int)_inArray[child])
                    swap = child;

                if( child+1 <= end && (int)_inArray[swap] < (int)_inArray[child+1])
                    swap = child + 1;

                if( swap != root )
                {
                    Swap(root, swap);
                    root = swap;
                }
                else
                    break;
            }

        }

        private void Swap(int i, int j)
        {
            var tmp = _inArray[i];
            _inArray[i] = _inArray[j];
            _inArray[j] = tmp;
        }
    }
}
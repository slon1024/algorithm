using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Xml.Linq;


namespace Sort
{
    class Program
    {
        static void Main(string[] args)
        {
            
            var arrays = new ArrayList() { 5, 8, 9, 1, 3, 0, 4 };
            Display(arrays);
            var mgrSort = new MergeSort();
            Display( mgrSort.Sort(arrays) );
           
            Console.ReadKey();
        }
        
        private static void Display(ArrayList arrays)
        {
            foreach (int value in arrays)
            {
                Console.Write(value);
            }
            Console.WriteLine();
        }
    }

    class Common
    {
        public delegate bool intFilter(int i);

        public int[] Fiters(int[] nums, intFilter filter)
        {
            ArrayList result = new ArrayList();

            foreach(int num in nums)
                if( filter(num) )
                    result.Add(num);
            return (int[])result.ToArray(typeof(int));
        }
    }
}

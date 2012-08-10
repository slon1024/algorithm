using System;
using System.Collections;

namespace Sort
{
    class Program
    {
        public delegate void MySort();

        public static void Main()
        {
            var values = new ArrayList();
            var randomNumber = new Random();
            for (int i = 0; i < 100; i++)
                values.Add(randomNumber.Next(1, 1000));


            Sort(new MergeSort(), values);
            Console.ReadKey();
        }

        public static void Sort(ISort sort, ArrayList inArray)
        {
            var result = sort.Sort(inArray);
            Console.WriteLine(result.ToString().Split(' '));
        }
    }
}

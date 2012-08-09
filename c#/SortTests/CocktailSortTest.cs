using System;
using System.Collections;
using NUnit.Framework;
using Sort;

namespace SortTests
{
    class CocktailSortTest
    {
        private ArrayList _values = new ArrayList();

        [SetUp]
        public void SetUp()
        {
            Random randomNumber = new Random();
            for (int i = 0; i < 100; i++)
                _values.Add(randomNumber.Next(1, 1000));
        }

        [Test]
        public void testSort()
        {
            var expected = (ArrayList)_values.Clone();
            expected.Sort();

            var cocktailSort = new CocktailSort();
            var actual = cocktailSort.Sort(_values);
            
            Assert.AreEqual(expected, actual);
        }
    }
    
}

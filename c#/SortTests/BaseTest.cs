using System;
using System.Collections;
using NUnit.Framework;
using Sort;

namespace SortTests
{
    abstract public class BaseTest
    {
        protected readonly ArrayList _values = new ArrayList();
        protected ISort _sort;

        [SetUp]
        public void SetUp()
        {
            var randomNumber = new Random();
            for (int i = 0; i < 100; i++)
                _values.Add(randomNumber.Next(1, 1000));
            
        }

    }
}

#include <iostream>

class IntArray
{
    private:
    int* m_ptr{nullptr};
    int m_size{0};

    public:
    IntArray() = default;
    explicit IntArray(int size)
    {
        if (size != 0)
        {
            m_ptr = new int[size]{};
            m_size = size;
        }
    }

    ~IntArray()
    {
        delete[] m_ptr;
        m_ptr = nullptr;
    }

    int Size() const
    {
        return m_size;
    }

    bool IsEmpty() const
    {
        return (m_size == 0);
    }

    int& operator[](int index)
    {
        return m_ptr[index];
    }
};
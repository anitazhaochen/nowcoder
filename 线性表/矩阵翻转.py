#!/usr/bin/python env
# coding:utf8

class Transform:
    def transformImage(self, mat, n):
        # write code here
        for i in range(n-1):
            for j in range(n-i-1):
                mat[i][j], mat[n-j-1][n-i-1] = mat[n-j-1][n-i-1], mat[i][j]

        for i in range(n//2):
            mat[i], mat[n-1-i] = mat[n-1-i], mat[i]

        return mat



Transform().transformImage([[1,2,3],[4,5,6],[7,8,9]],3)

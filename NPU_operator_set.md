# NPU Operator Set

* 目前适用于NPU的算子包括：
  
  * <a href="#VMM">VMM</a>
  * <a href="#Maxpool">Maxpool</a>
  
  * <a href="#Averagepool">Averagepool</a>
  * <a href="#Relu">Relu</a>
  
  * <a href="#Add (in tile)">Add (in tile)</a>
  * <a href="#Dimensional transformation">Dimensional transformation</a>



## 算子介绍
### <a name="VMM"></a><a name="VMM">**VMM**</a>

  VMM算子执行矩阵矢量乘法操作，可以将一个N列输入向量`X`和一个NxM的输入矩阵`A`进行点积运算得到一个M列的输出向量`Y`，过程满足等式：`Y=X·A`，由于输入向量与输入矩阵相乘的精度比输出向量的精度高，所以使用`numb`表示输出结果取的位数，`numstart`表示从理想输出精度的第几位开始取值来表示最终的输出向量的结果。

#### Attributes

<dl>
<dt><tt>numb</tt> : int</dt>
<dd>输出向量<b>Y</b>的精度，默认为<B>8</B>位</dd>
</dl>

<dl>
<dt><tt>numstart</tt> : float</dt>
<dd>从理想输出中取值表示输出向量<b>Y</b>的起始位，默认值为<b>12+log<sub>2</sub>(N)-8</b>，其中N为输入向量的列数</dd>
</dl>

#### Inputs

<dl>
<dt><tt>X</tt> : V1</dt>
<dd>N列输入向量，单个阵列运算时N最大值为<B>320</B></dd>
</dl>

<dl>
<dt><tt>A</tt> : M</dt>
<dd>NxM输入矩阵，单个阵列运算时M最大值为<B>320</B></dd>
</dl>



#### Outputs

<dl>
<dt><tt>Y</tt> : V2</dt>
<dd>M列输出向量</dd>
</dl>



#### Type Constraints

<dl>
<dt><tt>V1</tt> : 向量(uint8)</dt>
<dd>限制所有的输入向量的元素都为无符号的8bit的整数</dd>
</dl>

<dl>
<dt><tt>M</tt> : 矩阵(int4)</dt>
<dd>限制所有的输入矩阵的元素都为4bit的整数</dd>
</dl>
<dl>
<dt><tt>V2</tt> : 向量(int)</dt>
<dd>限制所有的输出向量的元素都为整型</dd>
</dl>


### <a name="Maxpool"></a><a name="Maxpool">**Maxpool**</a>

Maxpool算子是以池化区域最大值作为结果执行池化操作，可以将一个输入张量X按池化区域的大小(kernel sizes)以及池化步长(stride sizes)找出每个池化区域内的最大值然后组合成一个新的张量Y。

#### Attributes

<dl>
<dt><tt>kernel_size</tt> : int</dt>
<dd>默认值为2，可自定义</dd>
</dl>

<dl>
<dt><tt>stride_size</tt> : int</dt>
<dd>默认值为2，可自定义</dd>
</dl>

#### Inputs

<dl>
<dt><tt>X</tt> : T</dt>
<dd>输入张量</dd>
</dl>


#### Outputs

<dl>
<dt><tt>Y</tt> : T</dt>
<dd>输出张量</dd>
</dl>


#### Type Constraints

<dl>
<dt><tt>T</tt> : 张量(int8)</dt>
<dd>限制张量中所有的元素都为8bit的整数</dd>
</dl>



### <a name="Averagepool"></a><a name="Averagepool">**Averagepool**</a>

Averagepool算子是以池化区域的平均值作为结果执行池化操作，可以将一个输入张量X按池化区域的大小(kernel sizes)以及池化步长(stride sizes)计算每个池化区域内的平均值然后组合成一个新的张量Y

#### Attributes

<dl>
<dt><tt>kernel_size</tt> : int</dt>
<dd>默认值为2，可自定义</dd>
</dl>

<dl>
<dt><tt>stride_size</tt> : int</dt>
<dd>默认值为2，可自定义</dd>
</dl>

#### Inputs

<dl>
<dt><tt>X</tt> : T</dt>
<dd>输入张量</dd>
</dl>


#### Outputs

<dl>
<dt><tt>Y</tt> : T</dt>
<dd>输出张量</dd>
</dl>


#### Type Constraints

<dl>
<dt><tt>T</tt> : 张量(int8)</dt>
<dd>限制张量中所有元素都为8bit的整数</dd>
</dl>



### a name="Relu"></a><a name="Relu">**Relu**</a>

Relu算子可以将一个输入向量通过Relu函数[y=max(0,x)]后产生一个输出向量

#### Input

<dl>
<dt><tt>X</tt> : V</dt>
<dd>输入向量，大小暂时未定</dd>
</dl>



#### Output

<dl>
<dt><tt>Y</tt> : V</dt>
<dd>输出向量</dd>
</dl>


#### Type Constraints

<dl>
<dt><tt>V</tt> : 向量(int8)</dt>
<dd>限制向量中的所有元素都为8bit整数</dd>
</dl>


### <a name="Add (in tile)"></a><a name="Add (in tile)">**Add (in tile)**</a>

Add (in tile)算子可以将两个输入向量`X1`与`X2`相加后产生一个输出向量`Y`，满足等式`Y=X1+X2`，主要处理同一`tile`内部的加法运算

#### Input

<dl>
<dt><tt>X1</tt> : V</dt>
<dd>输入向量，大小暂时未定</dd>
</dl>

<dl>
<dt><tt>X2</tt> : V</dt>
<dd>输入向量，大小暂时未定</dd>
</dl>

#### Output

<dl>
<dt><tt>Y</tt> : V</dt>
<dd>输出向量</dd>
</dl>



#### Type Constraints

<dl>
<dt><tt>V</tt> : 向量(int8)</dt>
<dd>限制向量中的所有元素都为8bit整数</dd>
</dl>


### <a name=" Dimensional transformation"></a><a name="Dimensional transformation">**Dimensional transformation**</a>

Dimensional transformation算子可以将高维的输入张量`X`通过变化后产生一个低维的输出张量`Y`，主要是将输入的4维图像信息转化为2维的全连接层信息。

#### Input

<dl>
<dt><tt>X</tt> : T</dt>
<dd>输入张量，对于图像信息，输入为4维<b>NxCxHxW</b>,其中N为batch_size，C是通道数量，H，W分别为图像的高度和宽度。</dd>
</dl>



#### Output

<dl>
<dt><tt>Y</tt> : T</dt>
<dd>输出张量为2维<B>NxD</B>，其中N为batch_size，D=CxHxW</dd>
</dl>



#### Type Constraints

<dl>
<dt><tt>T</tt> : 张量(int8)</dt>
<dd>限制张量中的所有元素都为8bit整数</dd>
</dl>




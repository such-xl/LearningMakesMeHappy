#include"Exercises.h"
#pragma once
/***************************************************************************************************************************
											  ��������ϰ1��
									ͼ����̬ѧ�����ֱ��ͼ����и�ʴ�����͡������㡢������
*******************************************************************************************************************************/
void morphology()
{
	//��ȡͼƬ��ת��Ϊ�Ҷ�ͼ
	Mat srcMat = imread("res/pic/coin.png", 0);

	//�ж϶�ȡͼƬ�Ƿ�ʧ��
	if (srcMat.empty()) {
		cout << "fail to read pic!" << endl;
		return;
	}
	//����ͼ������
	Mat thresh_Mat;
	Mat dilate_Mat;
	Mat erode_Mat;
	Mat open_Mat;
	Mat close_Mat;

	//��ֵ��
	threshold(srcMat, thresh_Mat, 100, 255, THRESH_OTSU);

	/************************************************
	getStructuringElement���� ����ģ�ͣ�
	getStructuringElement(int shape, Size ksize, Point anchor = Point(-1,-1));

	�������ܣ�
	. int shape: ��������ĵ�һ��������ʾ�ں˵���״����������״����ѡ�񡣾��Σ�MORPH_RECT;�����Σ�MORPH_CROSS;��Բ�Σ�MORPH_ELLIPSE;
	. Size ksize: �ں˵ĳߴ�
	. Point anchor: ê���λ��
	**************************************************/
	//����ṹԪ��
	Mat element = getStructuringElement(MORPH_RECT, Size(5, 5), Point(-1, -1));

	//��ʴ
	/************************************************
	erode���� ����ģ�ͣ�
	 erode( InputArray src, OutputArray dst, InputArray kernel,
						 Point anchor = Point(-1,-1), int iterations = 1,
						 int borderType = BORDER_CONSTANT,
						 const Scalar& borderValue = morphologyDefaultBorderValue() );

	�������ܣ�
	. InputArray src: Mat�࣬ͨ���������ޣ������ӦΪCV_8U,CV_16U...
	. OutputArray dst: ���ͼ����Ҫ�к�ԭͼƬһ���ĳߴ������
	. InputArray kernel: ��ʴ�������ںˣ�һ����3*3�ĺ�
	. Point anchor:ê��λ�ã�һ���ã�-1��-1��
	.int iterations:ʹ�ú����Ĵ���
	.int borderType:�����ƶ�ͼ���ⲿ���ص�ĳ�ֱ߽�ģʽ
	. const Scalar& borderValue:�߽�Ϊ����ʱ�ı߽�ֵ

	**************************************************/

	erode(thresh_Mat, erode_Mat, element, Point(-1, -1), 1);

	//����
	/************************************************
	dialte���� ����ģ�ͣ�
	dilate( InputArray src, OutputArray dst, InputArray kernel,
						  Point anchor = Point(-1,-1), int iterations = 1,
						  int borderType = BORDER_CONSTANT,
						  const Scalar& borderValue = morphologyDefaultBorderValue() );

	�������ܣ�
	. InputArray src: Mat�࣬ͨ���������ޣ������ӦΪCV_8U,CV_16U...
	. OutputArray dst: ���ͼ����Ҫ�к�ԭͼƬһ���ĳߴ������
	. InputArray kernel: ��ʴ�������ںˣ�һ����3*3�ĺ�
	. Point anchor:ê��λ�ã�һ���ã�-1��-1��
	.int iterations:ʹ�ú����Ĵ���
	.int borderType:�����ƶ�ͼ���ⲿ���ص�ĳ�ֱ߽�ģʽ
	. const Scalar& borderValue:�߽�Ϊ����ʱ�ı߽�ֵ

	**************************************************/
	dilate(thresh_Mat, dilate_Mat, element, Point(-1, -1), 1);

	//������
	/************************************************
	 morphologyEx���� ����ģ�ͣ�
	 morphologyEx( InputArray src, OutputArray dst,
								int op, InputArray kernel,
								Point anchor = Point(-1,-1), int iterations = 1,
								int borderType = BORDER_CONSTANT,
								const Scalar& borderValue = morphologyDefaultBorderValue() );


	�������ܣ�
	. InputArray src: Mat�࣬ͨ���������ޣ������ӦΪCV_8U,CV_16U...
	. OutputArray dst: ���ͼ����Ҫ�к�ԭͼƬһ���ĳߴ������
	. int op:��ʾ��̬ѧ��������ͣ���MORPH_OPEN��MORPH_CLOSE�ֱ��������ͱ�����
	. InputArray kernel: ��ʴ�������ںˣ�һ����3*3�ĺ�
	. Point anchor:ê��λ�ã�һ���ã�-1��-1��
	. int iterations:ʹ�ú����Ĵ���
	. int borderType:�����ƶ�ͼ���ⲿ���ص�ĳ�ֱ߽�ģʽ
	. const Scalar& borderValue:�߽�Ϊ����ʱ�ı߽�ֵ

	**************************************************/
	morphologyEx(thresh_Mat, open_Mat, MORPH_OPEN, element, Point(-1, -1), 1);

	// ������
	morphologyEx(thresh_Mat, close_Mat, MORPH_CLOSE, element, Point(-1, -1), 1);


	//��ʾ���
	imshow("thresh_Mat", thresh_Mat);
	imshow("erode_Mat", erode_Mat);
	imshow("dilate_Mat", dilate_Mat);
	imshow("open_Mat", open_Mat);
	imshow("close_Mat", close_Mat);
	waitKey(0);
}

/***************************************************************************************************************************
													��������ϰ2��
													��ͨ����
***************************************************************************************************************************/
void connectedwithstats()
{
	//��ȡͼƬ��ת��Ϊ�Ҷ�ͼ
	Mat srcMat = imread("res/pic/coin.png");

	//�ж϶�ȡͼƬ�Ƿ�ʧ��
	if (srcMat.empty()) {
		cout << "fail to read pic!" << endl;
		return;
	}

	//ת��Ϊ�Ҷ�ͼ
	Mat gryMat;
	cvtColor(srcMat, gryMat, COLOR_BGRA2GRAY);

	//����ͼ������
	Mat stats;
	Mat centroids;
	Mat labels;
	Mat thresh_Mat;
	Mat open_Mat;

	//��򷨴���ͼ��
	threshold(gryMat, thresh_Mat, 100, 255, THRESH_OTSU);

	//����ṹԪ��
	Mat element = getStructuringElement(MORPH_RECT, Size(5, 5), Point(-1, -1));

	//������
	morphologyEx(thresh_Mat, open_Mat, MORPH_OPEN, element, Point(-1, -1), 1);
	


	//������ͨ����
	/************************************************
	connectedComponentsWithStats���� ����ģ�ͣ�
	connectedComponentsWithStats(InputArray image, OutputArray labels,
											  OutputArray stats, OutputArray centroids,
											  int connectivity = 8, int ltype = CV_32S);


	�������ܣ�
	. InputArray image: ����8λ��ͨ����ֵͼ��
	. OutputArray labels: �����ԭͼimageһ����ı��ͼ��label��Ӧ�ڱ�ʾ�ǵ�ǰ�����ǵڼ���������������0
	. OutputArray stats:���nccomps����ǩ������5�ľ��� ����ʾÿ����ͨ�������Ӿ��κ������pixel��
	. OutputArray centroids: ��Ӧ�������������ĵ㡣nccomps��2�ľ��� ��ʾÿ����ͨ���������
	. int connectivity:ʹ��8�������4����
	. int ltype:�����ǩ����������

	**************************************************/
	int nComp = connectedComponentsWithStats(open_Mat, labels, stats, centroids, 8, CV_32S);

	//��ȥ����0�������
	cout << "Ӳ�Ҹ���Ϊ��" << nComp - 1 << endl;

	//��ʶ�������ͨ�����С��ӱ߿�
	for (int i = 1; i < nComp; i++)
	{
		//����Rect��
		Rect bandbox;
		bandbox.x = stats.at<int>(i, 0);
		bandbox.y = stats.at<int>(i, 1);

		bandbox.width = stats.at<int>(i, 2);
		bandbox.height = stats.at<int>(i, 3);
		//��������
		/************************************************
		rectangle���� ����ģ�ͣ�
		rectangle(CV_IN_OUT Mat& img, Rect rec,
						  const Scalar& color, int thickness = 1,
						  int lineType = LINE_8, int shift = 0);

		�������ܣ�
		. ICV_IN_OUT Mat& img: CV_IN_OUT Mat& img
		. Rect rec: Rect���Ա���������ε����Ͻ������Լ�����
		. const Scalar& color:�����ɫ��Ϣ
		. int thickness: ��ʾ�ߵĴ�ϸ
		. int lineType :�ڽӹ�ϵ��һ������Ĭ��ֵ
		. int shift: ƫ�ƣ�һ����0
		**************************************************/
		rectangle(open_Mat, bandbox, 255, 1, 8, 0);
	}
	imshow("open_Mat", open_Mat);
	waitKey(0);
}




/***************************************************************************************************************************
													��������ϰ3��
													ԭ�����
***************************************************************************************************************************/

void origincount()
{
	//��ȡͼƬ��ת��Ϊ�Ҷ�ͼ
	Mat srcMat = imread("res/pic/originpoint.png");

	//�ж϶�ȡͼƬ�Ƿ�ʧ��
	if (srcMat.empty()) {
		cout << "fail to read pic!" << endl;
		return;
	}

	//ת��Ϊ�Ҷ�ͼ
	Mat gryMat;
	cvtColor(srcMat, gryMat, COLOR_BGRA2GRAY);

	//��ɫ
	gryMat = 255 - gryMat;

	Mat stats;
	Mat centroids;
	Mat labels;
	Mat thresh_Mat;
	Mat erode_Mat;

	//��򷨴���ͼ��
	threshold(gryMat, thresh_Mat, 100, 255, THRESH_OTSU);


	//����ṹԪ��
	Mat element = getStructuringElement(MORPH_RECT, Size(5, 5), Point(-1, -1));

	//��ͼ����и�ʴ����ֻ����Ҫ��ĵ�
	erode(thresh_Mat, erode_Mat, element, Point(-1, -1), 2);



	//������ͨ����
	int nComp = connectedComponentsWithStats(erode_Mat, labels, stats, centroids, 8, CV_32S);

	//��ȥ���������������
	cout << "ԭ�����Ϊ��" << nComp - 1 << endl;

}

/***************************************************************************************************************************
													��������ϰ4��
													���������
***************************************************************************************************************************/
void clipcount()
{
	//��ȡͼƬ��ת��Ϊ�Ҷ�ͼ
	Mat srcMat = imread("res/pic/clip.png");

	//�ж϶�ȡͼƬ�Ƿ�ʧ��
	if (srcMat.empty()) {
		cout << "fail to read pic!" << endl;
		return;
	}

	//ת��Ϊ�Ҷ�ͼ
	Mat gryMat;
	cvtColor(srcMat, gryMat, COLOR_BGRA2GRAY);

	//��ɫ
	gryMat = 255 - gryMat;

	Mat stats;
	Mat centroids;
	Mat labels;
	Mat thresh_Mat;
	Mat open_Mat;

	//��򷨴���ͼ��
	threshold(gryMat, thresh_Mat, 100, 255, THRESH_OTSU);


	//����ṹԪ��
	Mat element = getStructuringElement(MORPH_RECT, Size(3, 3), Point(-1, -1));

	//��ͼ����п����㴦������һЩ�ӵ�
	morphologyEx(thresh_Mat, open_Mat, MORPH_OPEN, element, Point(-1, -1), 1);



	//������ͨ����
	int nComp = connectedComponentsWithStats(open_Mat, labels, stats, centroids, 8, CV_32S);


	//�Ƚϳ���ȣ�ɸѡ��������ͨ��
	for (int i = 1; i < nComp; i++)
	{
		int width = stats.at<int>(i, 2);
		int height = stats.at<int>(i, 3);
		int ratio = height / width;
		if (ratio > 10)
		{
			nComp--;
		}
	}

	//��ȥ������ͨ���������������
	cout << "���������Ϊ��" << nComp - 1 << endl;

}


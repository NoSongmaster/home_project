���͵�ַ��http://www.cnblogs.com/NoSong/p/6365805.html
��ҵ��
��Ҫ��Ա����Ϣ�ļ���ʵ����ɾ�Ĳ����
�������ļ���main.py
ģ�����ݿ��ļ�:staff_database\user_database
ԭʼ�ļ���bak
�������ܣ�
������ҵһ��д��11��������
check_contain_chinese���������ַ��ǲ������ģ������������������
output_head���������selectͷ�����������
output_body: �������select���ݣ��������
output_tail: �����������������β�����ͳ���������������
show_user_list����ȡ���ݿ��ļ����ݣ��γ��б��㺯���������ݣ�
���ظ�ʽ��[{'staff_id': None, 'name': None, 'age': None, 'phone': None, 'dept': None, 'enroll_date': None},{2},{3},{...}]
check���������������жϣ�<��>��=��like��
add_user_list������������ݣ��жϼ����������ֻ����Ƿ���ڣ�������ʾ���ʧ�ܡ����뵽���ݿ��ļ���
select_search�����ڲ�ѯ���ݡ�
delete������ɾ�����ݣ��������ݿ��ļ���
modify�������޸����ݣ��������ݿ��ļ�
main:   �������塣������ɾ�Ĳ麯����

ʵ�ֹ��ܣ�
���Զ��ļ�������ɾ�Ĳ��������<>=likeȫ��ʵ�֡�
add_user_list() �жϼ����������ֻ����Ƿ���ڡ�phoneΪΨһ��
deleteɾ��ʱ�����������ʱ��staff_id Ϊ����id
modify()�����������޸�staff_id �� phone
���ԶԶ�����ݿ��ļ����в���


������
             select * from user_database
             select staff_id,name,age from user_database where dept like 'ʵϰ'
             insert into user_database value(alex,33,11111,teacher,2017-1-1)
             delete from user_database where staff_id > '10'
             update user_database set age = 100 where age = 77



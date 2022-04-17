--
-- PostgreSQL database dump
--

-- Dumped from database version 12.4
-- Dumped by pg_dump version 12.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: ads_ad; Type: TABLE; Schema: public; Owner: skypro_l28
--

CREATE TABLE public.ads_ad (
    id bigint NOT NULL,
    name character varying(100) NOT NULL,
    price integer NOT NULL,
    description text,
    image character varying(100) NOT NULL,
    is_published character varying(13) NOT NULL,
    author_id bigint NOT NULL,
    category_id bigint NOT NULL,
    CONSTRAINT ads_ad_price_check CHECK ((price >= 0))
);


ALTER TABLE public.ads_ad OWNER TO skypro_l28;

--
-- Name: ads_ad_id_seq; Type: SEQUENCE; Schema: public; Owner: skypro_l28
--

CREATE SEQUENCE public.ads_ad_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ads_ad_id_seq OWNER TO skypro_l28;

--
-- Name: ads_ad_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: skypro_l28
--

ALTER SEQUENCE public.ads_ad_id_seq OWNED BY public.ads_ad.id;


--
-- Name: ads_author; Type: TABLE; Schema: public; Owner: skypro_l28
--

CREATE TABLE public.ads_author (
    id bigint NOT NULL,
    first_name character varying(20) NOT NULL,
    last_name character varying(20) NOT NULL,
    username character varying(20) NOT NULL,
    password character varying(20) NOT NULL,
    role character varying(10) NOT NULL,
    age integer NOT NULL,
    CONSTRAINT ads_author_age_check CHECK ((age >= 0))
);


ALTER TABLE public.ads_author OWNER TO skypro_l28;

--
-- Name: ads_author_id_seq; Type: SEQUENCE; Schema: public; Owner: skypro_l28
--

CREATE SEQUENCE public.ads_author_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ads_author_id_seq OWNER TO skypro_l28;

--
-- Name: ads_author_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: skypro_l28
--

ALTER SEQUENCE public.ads_author_id_seq OWNED BY public.ads_author.id;


--
-- Name: ads_author_location_id; Type: TABLE; Schema: public; Owner: skypro_l28
--

CREATE TABLE public.ads_author_location_id (
    id bigint NOT NULL,
    author_id bigint NOT NULL,
    location_id bigint NOT NULL
);


ALTER TABLE public.ads_author_location_id OWNER TO skypro_l28;

--
-- Name: ads_author_location_id_seq; Type: SEQUENCE; Schema: public; Owner: skypro_l28
--

CREATE SEQUENCE public.ads_author_location_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ads_author_location_id_seq OWNER TO skypro_l28;

--
-- Name: ads_author_location_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: skypro_l28
--

ALTER SEQUENCE public.ads_author_location_id_seq OWNED BY public.ads_author_location_id.id;


--
-- Name: ads_category; Type: TABLE; Schema: public; Owner: skypro_l28
--

CREATE TABLE public.ads_category (
    id bigint NOT NULL,
    name character varying(120) NOT NULL
);


ALTER TABLE public.ads_category OWNER TO skypro_l28;

--
-- Name: ads_category_id_seq; Type: SEQUENCE; Schema: public; Owner: skypro_l28
--

CREATE SEQUENCE public.ads_category_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ads_category_id_seq OWNER TO skypro_l28;

--
-- Name: ads_category_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: skypro_l28
--

ALTER SEQUENCE public.ads_category_id_seq OWNED BY public.ads_category.id;


--
-- Name: ads_location; Type: TABLE; Schema: public; Owner: skypro_l28
--

CREATE TABLE public.ads_location (
    id bigint NOT NULL,
    name character varying(50) NOT NULL,
    lat numeric(8,6),
    lng numeric(8,6)
);


ALTER TABLE public.ads_location OWNER TO skypro_l28;

--
-- Name: ads_location_id_seq; Type: SEQUENCE; Schema: public; Owner: skypro_l28
--

CREATE SEQUENCE public.ads_location_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.ads_location_id_seq OWNER TO skypro_l28;

--
-- Name: ads_location_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: skypro_l28
--

ALTER SEQUENCE public.ads_location_id_seq OWNED BY public.ads_location.id;


--
-- Name: auth_group; Type: TABLE; Schema: public; Owner: skypro_l28
--

CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);


ALTER TABLE public.auth_group OWNER TO skypro_l28;

--
-- Name: auth_group_id_seq; Type: SEQUENCE; Schema: public; Owner: skypro_l28
--

CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_id_seq OWNER TO skypro_l28;

--
-- Name: auth_group_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: skypro_l28
--

ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;


--
-- Name: auth_group_permissions; Type: TABLE; Schema: public; Owner: skypro_l28
--

CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_group_permissions OWNER TO skypro_l28;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: skypro_l28
--

CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_group_permissions_id_seq OWNER TO skypro_l28;

--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: skypro_l28
--

ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;


--
-- Name: auth_permission; Type: TABLE; Schema: public; Owner: skypro_l28
--

CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);


ALTER TABLE public.auth_permission OWNER TO skypro_l28;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE; Schema: public; Owner: skypro_l28
--

CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_permission_id_seq OWNER TO skypro_l28;

--
-- Name: auth_permission_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: skypro_l28
--

ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;


--
-- Name: auth_user; Type: TABLE; Schema: public; Owner: skypro_l28
--

CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);


ALTER TABLE public.auth_user OWNER TO skypro_l28;

--
-- Name: auth_user_groups; Type: TABLE; Schema: public; Owner: skypro_l28
--

CREATE TABLE public.auth_user_groups (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);


ALTER TABLE public.auth_user_groups OWNER TO skypro_l28;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE; Schema: public; Owner: skypro_l28
--

CREATE SEQUENCE public.auth_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_groups_id_seq OWNER TO skypro_l28;

--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: skypro_l28
--

ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;


--
-- Name: auth_user_id_seq; Type: SEQUENCE; Schema: public; Owner: skypro_l28
--

CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_id_seq OWNER TO skypro_l28;

--
-- Name: auth_user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: skypro_l28
--

ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;


--
-- Name: auth_user_user_permissions; Type: TABLE; Schema: public; Owner: skypro_l28
--

CREATE TABLE public.auth_user_user_permissions (
    id bigint NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);


ALTER TABLE public.auth_user_user_permissions OWNER TO skypro_l28;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE; Schema: public; Owner: skypro_l28
--

CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.auth_user_user_permissions_id_seq OWNER TO skypro_l28;

--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: skypro_l28
--

ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;


--
-- Name: django_admin_log; Type: TABLE; Schema: public; Owner: skypro_l28
--

CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);


ALTER TABLE public.django_admin_log OWNER TO skypro_l28;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE; Schema: public; Owner: skypro_l28
--

CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_admin_log_id_seq OWNER TO skypro_l28;

--
-- Name: django_admin_log_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: skypro_l28
--

ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;


--
-- Name: django_content_type; Type: TABLE; Schema: public; Owner: skypro_l28
--

CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);


ALTER TABLE public.django_content_type OWNER TO skypro_l28;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE; Schema: public; Owner: skypro_l28
--

CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_content_type_id_seq OWNER TO skypro_l28;

--
-- Name: django_content_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: skypro_l28
--

ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;


--
-- Name: django_migrations; Type: TABLE; Schema: public; Owner: skypro_l28
--

CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);


ALTER TABLE public.django_migrations OWNER TO skypro_l28;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE; Schema: public; Owner: skypro_l28
--

CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.django_migrations_id_seq OWNER TO skypro_l28;

--
-- Name: django_migrations_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: skypro_l28
--

ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;


--
-- Name: django_session; Type: TABLE; Schema: public; Owner: skypro_l28
--

CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);


ALTER TABLE public.django_session OWNER TO skypro_l28;

--
-- Name: ads_ad id; Type: DEFAULT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.ads_ad ALTER COLUMN id SET DEFAULT nextval('public.ads_ad_id_seq'::regclass);


--
-- Name: ads_author id; Type: DEFAULT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.ads_author ALTER COLUMN id SET DEFAULT nextval('public.ads_author_id_seq'::regclass);


--
-- Name: ads_author_location_id id; Type: DEFAULT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.ads_author_location_id ALTER COLUMN id SET DEFAULT nextval('public.ads_author_location_id_seq'::regclass);


--
-- Name: ads_category id; Type: DEFAULT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.ads_category ALTER COLUMN id SET DEFAULT nextval('public.ads_category_id_seq'::regclass);


--
-- Name: ads_location id; Type: DEFAULT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.ads_location ALTER COLUMN id SET DEFAULT nextval('public.ads_location_id_seq'::regclass);


--
-- Name: auth_group id; Type: DEFAULT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);


--
-- Name: auth_group_permissions id; Type: DEFAULT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);


--
-- Name: auth_permission id; Type: DEFAULT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);


--
-- Name: auth_user id; Type: DEFAULT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);


--
-- Name: auth_user_groups id; Type: DEFAULT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);


--
-- Name: auth_user_user_permissions id; Type: DEFAULT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);


--
-- Name: django_admin_log id; Type: DEFAULT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);


--
-- Name: django_content_type id; Type: DEFAULT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);


--
-- Name: django_migrations id; Type: DEFAULT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);


--
-- Data for Name: ads_ad; Type: TABLE DATA; Schema: public; Owner: skypro_l28
--

COPY public.ads_ad (id, name, price, description, image, is_published, author_id, category_id) FROM stdin;
2	Стратегия голубого океана	650	Твердый переплет, состояние прекрасное. По всем вопросам лучше писать, звонок могу не услышать. Передам у м. Студенческая.	images/post2.png	TRUE	1	3
3	Принципы, Рэй Далио	555	Твердый переплет, состояние хорошее. Встречусь у метро у м. Черкизоская или на кольцевой.	images/post3.png	TRUE	5	3
4	Разумный инвестор	250	Твердый переплет, состояние нормальное. Встречусь у метро у м. Черкизоская или на кольцевойе	images/post4.jpg	TRUE	5	3
5	Розанов В. В. Уединенное	100	Передам на Чернышевской, по вопросам - лучше звоните.	images/post5.png	TRUE	10	3
6	Alice Sebold - The lovely bone	250	Идеально для изучения языка, книга в хорошем состоянии без пометок карандашом. Книга в мягком переплете (!!). Передам у метро.	images/post6.jpg	TRUE	8	3
7	Котята в добрые руки	100	Котята из приюта. Ласковые и адаптированые. Лоток знают на 5, стоят все прививки. Готовые перезжать в новый дом. Больше фотографий скину в личку)	images/post7.jpg	TRUE	5	1
8	Молодая кошечка Груша	100	Груша - сладкая, яркая и очень милая кошка! Предпочитает держаться отстраненно, но мы уверены, что в жизни каждой пугливой кошки рано или поздно появляется человек, которому они будут доверять. Давайте поможем ей найти такого человека! Отдается под договор с ненавязчивым отслеживанием.	images/post8.jpg	TRUE	5	1
9	Собака в добрые руки	150	Знакомьтесь - Шери! Ищет хозяев, для которых была бы единственной любимицей, так как делить внимание и любовь хозяина с другими животными ей совсем не хочется. Отдается под договор с ненавязчивым отслеживанием.	images/post9.jpg	TRUE	5	2
10	Собака Дуся в добрые руки	150	История её попадания в приют стара, как мир: жил был добрый человек, который очень любил животных и в один миг всё закончилось...вместо радости и любви в их дом пришла смерть 😔  Давайте вместе найдём для Бабуси Дуси новый дом или хотя бы передержку...она замечательная, добрая и милая собака, которая точно заслуживает второго шанса на счастливую жизнь! 🙏🏻 Отдается под договор с ненавязчивым отслеживанием.	images/post10.jpg	FALSE	5	2
11	Стол из слэба и эпоксидной смолы	24000		images/post11.jpg	TRUE	6	5
12	Собака в добрые руки	1500	Весенняя и лукавая Норочка не унывает и терпеливо ждёт единственного и неповторимого хозяина! Нора - собака для тепла, любви и активного времяпрепровождения! Если Вы давно ищите компаньона и друга, то Нора очень Вас ждёт!	images/post12.jpg	TRUE	6	2
13	Метис овчарки в добрые руки	400	Роксана - идеальная собака для спокойных людей, которые любят проводить тихие вечера дома перед телевизором или за чтением книжки. Роксана очень зависит от человека, привязывается, доверяет и готова всегда ходить хвостиком. Роксана очень любит спокойствие, тишину, не любит плохую погоду и длительные прогулки. Девочка молода, стерилизована, привита, здорова!	images/post13.jpg	TRUE	7	2
14	Черенки петунии, рассада цветов, овощей	120	Принимаем заказы на 2022 год на укоренённые черенки ампельной петунии\n(более 30 сортов) и других цветов.	images/post14.jpg	TRUE	7	4
15	Гардения Жасминовидная	550	Гардения Жасминовая\nОчень ароматные Цветы (запах зелёного чая).\nЛюбой кустик 550₽.	images/post15.jpg	TRUE	7	4
16	Петуния, крейзитуния, бленкет, сурфиния, калиб	89	Продам черенки петунии крейзитунии, сурфинии, петхоа, калибрахоа, каскадиас, тамбелина, бьютикал, бони, бленкет. Цена 89 р.	images/post16.jpg	TRUE	10	4
17	Добрый песик ищет хозяина	150	Ерёма - коник в миниатюре! Славный, смешной и очень активный, он ищет хозяев, которые бы смогли дать ему достаточное количество прогулок на свежем воздухе, задорных игр и внимания, которое он так заслуживает. Ерёма совсем молодой, ему около года. Он приучен к домашней жизни и выгулу на улице. При первом знакомстве он может немного сторониться новых людей, но это быстро пройдет, стоит ему лишь получше Вас узнать. Такое чудо заслуживает замечательных хозяев!	images/post17.jpg	FALSE	10	2
18	Стол лофт большой	13800	Стол отлично подойдёт как под обеденный так и для переговоров, размер 200/100 см, высота стандартная 75 см. Выполнен из массива сосны. Можно сделать также из ясеня, дуба.	images/post18.jpg	TRUE	1	5
19	Стол прямой прям хороший	1800	Продаю столы потому что остались не востребоваными. Лишки компании. Ушли на удаленку. Размеры : 140/70 см. Всего 4-6 шт. Так же есть такого цвета и другая мебель. СМОТРИТЕ В ПРОФИЛЕ МОЕМ.	images/post19.jpg	TRUE	10	5
20	Котенок в добрые руки	100	Сатоши Пеструшкин - спасённый из подвала малыш, которому последнему из братьев посчастливилось оказаться на передержке! Его братцы уже дома, а Сатоши только-только начинает свой путь. Ему около 2 месяцев, он уже прошел карантин и активно обучается хорошим манерам. Котёнок очень спокойный, немного робкий и стеснительный, но в любящих руках он нежно и ласково мурчит! Пишите нам в сообщения и приезжайте знакомиться.	images/post20.jpg	TRUE	7	1
1	Сибирская котята, 3 месяца	2500	Продаю сибирских котят, возвраст 3 месяца.\r\nОчень милые и ручные.\r\nЛоточек знают на пятерку, кушают премиум корм.\r\nЖдут любящих и заботливых хояев. Больше фотографий отправлю в личку, цена указана за 1 котенка.	images/photo_2022-04-04_18-51-54.jpg	TRUE	1	1
\.


--
-- Data for Name: ads_author; Type: TABLE DATA; Schema: public; Owner: skypro_l28
--

COPY public.ads_author (id, first_name, last_name, username, password, role, age) FROM stdin;
1	Павел	Никифоров	pnikifirov	gZvptL	member	21
2	Альбина	Игнатьева	abiba_1341	4fVqL2	moderator	24
3	Иван	Сысоев	vanya777	o535pj	admin	29
4	Марина	Беркутова	orlanfree	d49rSO	moderator	19
5	Галина	Иванова	galina_ivanova	wCqlVE	member	41
6	Петр	Бойченко	petr_bo	xuR2jf	member	37
7	Никита		nikitapro	gzP4vR	member	26
8	Виолетта	Петушок	riverna	zo0rj6	member	24
9	Гульнара	Ибрагимова	gulnara321	daMocL	moderator	22
10	Борис	Зайка	dragon84	sasha123456	member	35
19	Павел	Александров	palexandrov	password	member	18
\.


--
-- Data for Name: ads_author_location_id; Type: TABLE DATA; Schema: public; Owner: skypro_l28
--

COPY public.ads_author_location_id (id, author_id, location_id) FROM stdin;
3	1	1
4	1	2
5	2	3
6	3	8
7	4	10
8	5	2
9	6	4
10	7	7
11	8	5
12	9	9
13	10	6
33	19	15
34	19	16
\.


--
-- Data for Name: ads_category; Type: TABLE DATA; Schema: public; Owner: skypro_l28
--

COPY public.ads_category (id, name) FROM stdin;
2	Песики
3	Книги
4	Растения
5	Мебель и интерьер
1	котики
10	test11
\.


--
-- Data for Name: ads_location; Type: TABLE DATA; Schema: public; Owner: skypro_l28
--

COPY public.ads_location (id, name, lat, lng) FROM stdin;
1	Москва, м. Студенческая	55.738472	37.548188
2	Москва, м. Черкизовская	55.804042	37.745415
3	Санкт-Петербург, м. Невский проспект	59.934719	30.331599
4	Москва, м. Библиотека имени Ленина	55.751275	37.610953
5	Москва, м. Комсомольская	55.775256	37.655653
6	Санкт-Петербург, м. Чернышевская	59.946097	30.371087
7	Пушкин, Павловское шоссе 23/2	59.707737	30.415887
8	Сакнт-Петербург, м. Балтийская	59.910822	30.327827
9	Москва, м. Беломорская	55.865056	37.475797
10	Москва, м. Электрозаодская	55.781876	7.705322
11	тест Москва	55.781877	55.770532
13	Москва	\N	\N
14	м. Авиастроительная	\N	\N
15	Москва, м. оморская	\N	\N
16	Москва, м. Тестовая	\N	\N
\.


--
-- Data for Name: auth_group; Type: TABLE DATA; Schema: public; Owner: skypro_l28
--

COPY public.auth_group (id, name) FROM stdin;
\.


--
-- Data for Name: auth_group_permissions; Type: TABLE DATA; Schema: public; Owner: skypro_l28
--

COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
\.


--
-- Data for Name: auth_permission; Type: TABLE DATA; Schema: public; Owner: skypro_l28
--

COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
1	Can add log entry	1	add_logentry
2	Can change log entry	1	change_logentry
3	Can delete log entry	1	delete_logentry
4	Can view log entry	1	view_logentry
5	Can add permission	2	add_permission
6	Can change permission	2	change_permission
7	Can delete permission	2	delete_permission
8	Can view permission	2	view_permission
9	Can add group	3	add_group
10	Can change group	3	change_group
11	Can delete group	3	delete_group
12	Can view group	3	view_group
13	Can add user	4	add_user
14	Can change user	4	change_user
15	Can delete user	4	delete_user
16	Can view user	4	view_user
17	Can add content type	5	add_contenttype
18	Can change content type	5	change_contenttype
19	Can delete content type	5	delete_contenttype
20	Can view content type	5	view_contenttype
21	Can add session	6	add_session
22	Can change session	6	change_session
23	Can delete session	6	delete_session
24	Can view session	6	view_session
25	Can add category	7	add_category
26	Can change category	7	change_category
27	Can delete category	7	delete_category
28	Can view category	7	view_category
29	Can add location	8	add_location
30	Can change location	8	change_location
31	Can delete location	8	delete_location
32	Can view location	8	view_location
33	Can add author	9	add_author
34	Can change author	9	change_author
35	Can delete author	9	delete_author
36	Can view author	9	view_author
37	Can add ad	10	add_ad
38	Can change ad	10	change_ad
39	Can delete ad	10	delete_ad
40	Can view ad	10	view_ad
\.


--
-- Data for Name: auth_user; Type: TABLE DATA; Schema: public; Owner: skypro_l28
--

COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
1	pbkdf2_sha256$320000$JJM1Tr1D5czhoH5pvYZW31$/ZV+liK1Nd/8P3Gek4O673ZwznAaNXNds4RorzgPZ6Y=	2022-04-16 15:08:32.559509+00	t	dalred				t	t	2022-04-16 15:07:56.410951+00
\.


--
-- Data for Name: auth_user_groups; Type: TABLE DATA; Schema: public; Owner: skypro_l28
--

COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
\.


--
-- Data for Name: auth_user_user_permissions; Type: TABLE DATA; Schema: public; Owner: skypro_l28
--

COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
\.


--
-- Data for Name: django_admin_log; Type: TABLE DATA; Schema: public; Owner: skypro_l28
--

COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
1	2022-04-16 15:37:45.027369+00	1	id=1.Сибирская котята, 3 месяца	2	[{"changed": {"fields": ["Description", "Image"]}}]	10	1
2	2022-04-16 15:45:04.020112+00	1	id=1.Сибирская котята, 3 месяца	2	[{"changed": {"fields": ["Image"]}}]	10	1
3	2022-04-16 18:08:18.058267+00	11	id=11.тест Москва	1	[{"added": {}}]	8	1
4	2022-04-16 18:08:23.305201+00	1	id=1.Павел	2	[{"changed": {"fields": ["Location"]}}]	9	1
\.


--
-- Data for Name: django_content_type; Type: TABLE DATA; Schema: public; Owner: skypro_l28
--

COPY public.django_content_type (id, app_label, model) FROM stdin;
1	admin	logentry
2	auth	permission
3	auth	group
4	auth	user
5	contenttypes	contenttype
6	sessions	session
7	ads	category
8	ads	location
9	ads	author
10	ads	ad
\.


--
-- Data for Name: django_migrations; Type: TABLE DATA; Schema: public; Owner: skypro_l28
--

COPY public.django_migrations (id, app, name, applied) FROM stdin;
1	contenttypes	0001_initial	2022-04-16 00:56:48.761063+00
2	auth	0001_initial	2022-04-16 00:56:48.975075+00
3	admin	0001_initial	2022-04-16 00:56:49.027659+00
4	admin	0002_logentry_remove_auto_add	2022-04-16 00:56:49.047657+00
5	admin	0003_logentry_add_action_flag_choices	2022-04-16 00:56:49.067658+00
6	ads	0001_initial	2022-04-16 00:56:49.159657+00
7	contenttypes	0002_remove_content_type_name	2022-04-16 00:56:49.204658+00
8	auth	0002_alter_permission_name_max_length	2022-04-16 00:56:49.229658+00
9	auth	0003_alter_user_email_max_length	2022-04-16 00:56:49.252662+00
10	auth	0004_alter_user_username_opts	2022-04-16 00:56:49.273659+00
11	auth	0005_alter_user_last_login_null	2022-04-16 00:56:49.296297+00
12	auth	0006_require_contenttypes_0002	2022-04-16 00:56:49.306296+00
13	auth	0007_alter_validators_add_error_messages	2022-04-16 00:56:49.325298+00
14	auth	0008_alter_user_username_max_length	2022-04-16 00:56:49.355307+00
15	auth	0009_alter_user_last_name_max_length	2022-04-16 00:56:49.387299+00
16	auth	0010_alter_group_name_max_length	2022-04-16 00:56:49.412297+00
17	auth	0011_update_proxy_permissions	2022-04-16 00:56:49.436296+00
18	auth	0012_alter_user_first_name_max_length	2022-04-16 00:56:49.458297+00
19	sessions	0001_initial	2022-04-16 00:56:49.495296+00
20	ads	0002_alter_ad_is_published	2022-04-16 02:57:17.04547+00
21	ads	0003_alter_ad_options_alter_author_options_and_more	2022-04-16 15:08:07.331706+00
22	ads	0004_remove_author_location_author_location	2022-04-16 18:17:50.793625+00
23	ads	0005_rename_location_author_location_id	2022-04-16 18:24:26.256914+00
24	ads	0006_alter_location_lat_alter_location_lng	2022-04-17 01:04:50.432248+00
25	ads	0007_alter_ad_options_alter_author_options_and_more	2022-04-17 02:54:04.679185+00
\.


--
-- Data for Name: django_session; Type: TABLE DATA; Schema: public; Owner: skypro_l28
--

COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
fsid2kdsttvrum5av7ypq7v8v3c7enqi	.eJxVjEEOwiAQRe_C2hBgykhduu8ZyMCAVA0kpV0Z765NutDtf-_9l_C0rcVvPS1-ZnERWpx-t0DxkeoO-E711mRsdV3mIHdFHrTLqXF6Xg_376BQL9_aMY8MHAwA2oygOFlFgDG6mNAY1EzsbBhyPqPSmUbOidwAKiLYHMT7A_diOJI:1nfhE8:GH1d34EMYi5BHc4IVpgxfSt3lQan9wSVXbokkX2d9CQ	2022-04-30 15:08:32.56555+00
\.


--
-- Name: ads_ad_id_seq; Type: SEQUENCE SET; Schema: public; Owner: skypro_l28
--

SELECT pg_catalog.setval('public.ads_ad_id_seq', 20, true);


--
-- Name: ads_author_id_seq; Type: SEQUENCE SET; Schema: public; Owner: skypro_l28
--

SELECT pg_catalog.setval('public.ads_author_id_seq', 19, true);


--
-- Name: ads_author_location_id_seq; Type: SEQUENCE SET; Schema: public; Owner: skypro_l28
--

SELECT pg_catalog.setval('public.ads_author_location_id_seq', 35, true);


--
-- Name: ads_category_id_seq; Type: SEQUENCE SET; Schema: public; Owner: skypro_l28
--

SELECT pg_catalog.setval('public.ads_category_id_seq', 10, true);


--
-- Name: ads_location_id_seq; Type: SEQUENCE SET; Schema: public; Owner: skypro_l28
--

SELECT pg_catalog.setval('public.ads_location_id_seq', 16, true);


--
-- Name: auth_group_id_seq; Type: SEQUENCE SET; Schema: public; Owner: skypro_l28
--

SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);


--
-- Name: auth_group_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: skypro_l28
--

SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);


--
-- Name: auth_permission_id_seq; Type: SEQUENCE SET; Schema: public; Owner: skypro_l28
--

SELECT pg_catalog.setval('public.auth_permission_id_seq', 40, true);


--
-- Name: auth_user_groups_id_seq; Type: SEQUENCE SET; Schema: public; Owner: skypro_l28
--

SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);


--
-- Name: auth_user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: skypro_l28
--

SELECT pg_catalog.setval('public.auth_user_id_seq', 1, true);


--
-- Name: auth_user_user_permissions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: skypro_l28
--

SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);


--
-- Name: django_admin_log_id_seq; Type: SEQUENCE SET; Schema: public; Owner: skypro_l28
--

SELECT pg_catalog.setval('public.django_admin_log_id_seq', 4, true);


--
-- Name: django_content_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: skypro_l28
--

SELECT pg_catalog.setval('public.django_content_type_id_seq', 10, true);


--
-- Name: django_migrations_id_seq; Type: SEQUENCE SET; Schema: public; Owner: skypro_l28
--

SELECT pg_catalog.setval('public.django_migrations_id_seq', 25, true);


--
-- Name: ads_ad ads_ad_pkey; Type: CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.ads_ad
    ADD CONSTRAINT ads_ad_pkey PRIMARY KEY (id);


--
-- Name: ads_author_location_id ads_author_location_author_id_location_id_605d3cdb_uniq; Type: CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.ads_author_location_id
    ADD CONSTRAINT ads_author_location_author_id_location_id_605d3cdb_uniq UNIQUE (author_id, location_id);


--
-- Name: ads_author_location_id ads_author_location_pkey; Type: CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.ads_author_location_id
    ADD CONSTRAINT ads_author_location_pkey PRIMARY KEY (id);


--
-- Name: ads_author ads_author_pkey; Type: CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.ads_author
    ADD CONSTRAINT ads_author_pkey PRIMARY KEY (id);


--
-- Name: ads_category ads_category_pkey; Type: CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.ads_category
    ADD CONSTRAINT ads_category_pkey PRIMARY KEY (id);


--
-- Name: ads_location ads_location_pkey; Type: CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.ads_location
    ADD CONSTRAINT ads_location_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_name_key; Type: CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);


--
-- Name: auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq; Type: CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);


--
-- Name: auth_group_permissions auth_group_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_group auth_group_pkey; Type: CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);


--
-- Name: auth_permission auth_permission_content_type_id_codename_01ab375a_uniq; Type: CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);


--
-- Name: auth_permission auth_permission_pkey; Type: CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_pkey; Type: CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);


--
-- Name: auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq; Type: CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);


--
-- Name: auth_user auth_user_pkey; Type: CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_pkey; Type: CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq; Type: CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);


--
-- Name: auth_user auth_user_username_key; Type: CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);


--
-- Name: django_admin_log django_admin_log_pkey; Type: CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);


--
-- Name: django_content_type django_content_type_app_label_model_76bd3d3b_uniq; Type: CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);


--
-- Name: django_content_type django_content_type_pkey; Type: CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);


--
-- Name: django_migrations django_migrations_pkey; Type: CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);


--
-- Name: django_session django_session_pkey; Type: CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);


--
-- Name: ads_ad_author_id_57b8bdcb; Type: INDEX; Schema: public; Owner: skypro_l28
--

CREATE INDEX ads_ad_author_id_57b8bdcb ON public.ads_ad USING btree (author_id);


--
-- Name: ads_ad_category_id_c50b5f67; Type: INDEX; Schema: public; Owner: skypro_l28
--

CREATE INDEX ads_ad_category_id_c50b5f67 ON public.ads_ad USING btree (category_id);


--
-- Name: ads_author_location_author_id_c66445e3; Type: INDEX; Schema: public; Owner: skypro_l28
--

CREATE INDEX ads_author_location_author_id_c66445e3 ON public.ads_author_location_id USING btree (author_id);


--
-- Name: ads_author_location_location_id_0d4e0a15; Type: INDEX; Schema: public; Owner: skypro_l28
--

CREATE INDEX ads_author_location_location_id_0d4e0a15 ON public.ads_author_location_id USING btree (location_id);


--
-- Name: auth_group_name_a6ea08ec_like; Type: INDEX; Schema: public; Owner: skypro_l28
--

CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);


--
-- Name: auth_group_permissions_group_id_b120cbf9; Type: INDEX; Schema: public; Owner: skypro_l28
--

CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);


--
-- Name: auth_group_permissions_permission_id_84c5c92e; Type: INDEX; Schema: public; Owner: skypro_l28
--

CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);


--
-- Name: auth_permission_content_type_id_2f476e4b; Type: INDEX; Schema: public; Owner: skypro_l28
--

CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);


--
-- Name: auth_user_groups_group_id_97559544; Type: INDEX; Schema: public; Owner: skypro_l28
--

CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);


--
-- Name: auth_user_groups_user_id_6a12ed8b; Type: INDEX; Schema: public; Owner: skypro_l28
--

CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);


--
-- Name: auth_user_user_permissions_permission_id_1fbb5f2c; Type: INDEX; Schema: public; Owner: skypro_l28
--

CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);


--
-- Name: auth_user_user_permissions_user_id_a95ead1b; Type: INDEX; Schema: public; Owner: skypro_l28
--

CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);


--
-- Name: auth_user_username_6821ab7c_like; Type: INDEX; Schema: public; Owner: skypro_l28
--

CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);


--
-- Name: django_admin_log_content_type_id_c4bce8eb; Type: INDEX; Schema: public; Owner: skypro_l28
--

CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);


--
-- Name: django_admin_log_user_id_c564eba6; Type: INDEX; Schema: public; Owner: skypro_l28
--

CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);


--
-- Name: django_session_expire_date_a5c62663; Type: INDEX; Schema: public; Owner: skypro_l28
--

CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);


--
-- Name: django_session_session_key_c0390e0f_like; Type: INDEX; Schema: public; Owner: skypro_l28
--

CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);


--
-- Name: ads_ad ads_ad_author_id_57b8bdcb_fk_ads_author_id; Type: FK CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.ads_ad
    ADD CONSTRAINT ads_ad_author_id_57b8bdcb_fk_ads_author_id FOREIGN KEY (author_id) REFERENCES public.ads_author(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ads_ad ads_ad_category_id_c50b5f67_fk_ads_category_id; Type: FK CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.ads_ad
    ADD CONSTRAINT ads_ad_category_id_c50b5f67_fk_ads_category_id FOREIGN KEY (category_id) REFERENCES public.ads_category(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ads_author_location_id ads_author_location_author_id_c66445e3_fk_ads_author_id; Type: FK CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.ads_author_location_id
    ADD CONSTRAINT ads_author_location_author_id_c66445e3_fk_ads_author_id FOREIGN KEY (author_id) REFERENCES public.ads_author(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: ads_author_location_id ads_author_location_location_id_0d4e0a15_fk_ads_location_id; Type: FK CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.ads_author_location_id
    ADD CONSTRAINT ads_author_location_location_id_0d4e0a15_fk_ads_location_id FOREIGN KEY (location_id) REFERENCES public.ads_location(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id; Type: FK CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm; Type: FK CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co; Type: FK CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;


--
-- Name: django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id; Type: FK CONSTRAINT; Schema: public; Owner: skypro_l28
--

ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;


--
-- PostgreSQL database dump complete
--


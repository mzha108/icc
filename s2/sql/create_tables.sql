CREATE TABLE [dbo].[DimSchool](	
	[SchoolKey] [int] IDENTITY(1,1) NOT NULL,
	[School_Id] [nvarchar](255) NULL,
	[postcode] [nvarchar](255) NULL,
	[School_Name] [nvarchar](255) NULL,
	[School_Address] [nvarchar](255) NULL,
	[Town_Suburb] [nvarchar](255) NULL,
	[School_Lat] [nvarchar](255) NULL,
	[School_Lon] [nvarchar](255) NULL,
	[Student_Number] [int] NULL,
	[ICSEA_Value] [int] NULL,
	[Level_Of_Schooling] [nvarchar](255) NULL,
	[School_Specialty_Type] [nvarchar](255) NULL,
	[School_Subtype] [nvarchar](255) NULL,
	[School_Gender] [nvarchar](255) NULL,
	[Late_Opening_School] [nvarchar](255) NULL,
	[1st_Teacher] [nvarchar](255) NULL,
	[State_Code] [nvarchar](255) NULL
 CONSTRAINT [PK_DimSchool] PRIMARY KEY CLUSTERED 	
(	
	[SchoolKey] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]	
) ON [PRIMARY]	


CREATE TABLE [dbo].[DimStation](	
	[StationKey] [int] IDENTITY(1,1) NOT NULL,
	[Station_Id] [nvarchar](MAX) NULL,
	[State_Code] [nvarchar](5) NULL,
	[postcode] [nvarchar](255) NULL,
	[Train_Station] [nvarchar](30) NULL,
	[Street_Name] [nvarchar](50) NULL,
	[Street_Type] [nvarchar](10) NULL,
	[Entrance_Type] [nvarchar](10) NULL,
	[School_Lat] [nvarchar](255) NULL,
	[School_Lon] [nvarchar](255) NULL
 CONSTRAINT [PK_DimStation] PRIMARY KEY CLUSTERED 	
(	
	[StationKey] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]	
) ON [PRIMARY]	


CREATE TABLE [dbo].[DimSuburb](	
	[SuburbKey] [int] IDENTITY(1,1) NOT NULL,
	[postcode] [nvarchar](10) NULL,
	[Suburb] [nvarchar](50) NULL,
	[City] [nvarchar](50) NULL,
	[State] [nvarchar](100) NULL,
	[State_Code] [nvarchar](5) NULL,
	[School_Lat] [nvarchar](255) NULL,
	[School_Lon] [nvarchar](255) NULL
 CONSTRAINT [PK_DimSuburb] PRIMARY KEY CLUSTERED 	
(	
	[SuburbKey] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]	
) ON [PRIMARY]	


CREATE TABLE [dbo].[DimProperty](	
	[PropertyKey] [int] IDENTITY(1,1) NOT NULL,
	[Property_Id] [nvarchar](MAX) NULL,
	[State] [nvarchar](100) NULL,
	[State_Code] [nvarchar](5) NULL,
	[City] [nvarchar](50) NULL,
	[Suburb] [nvarchar](50) NULL,
	[postcode] [nvarchar](10) NULL,
	[Updated_Year] [nvarchar](4) NULL,
	[Updated_Month] [nvarchar](2) NULL,
	[value] [float] NULL,
 CONSTRAINT [PK_DimProperty] PRIMARY KEY CLUSTERED 	
(	
	[PropertyKey] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]	
) ON [PRIMARY]	


CREATE TABLE [dbo].[DimAUS_SubCity](	
	[DimAUS_SubCityKey] [int] IDENTITY(1,1) NOT NULL,
	[Id] [nvarchar](MAX) NULL,
	[postcode] [nvarchar](255) NULL,
	[Suburb] [nvarchar](255) NULL,
	[City] [nvarchar](255) NULL,
	[State] [nvarchar](255) NULL,
	[State_Code] [nvarchar](2555) NULL,
	[lat] [nvarchar](255) NULL,
	[lon] [nvarchar](255) NULL,
	[Distric] [nvarchar] (255) NULL,
 CONSTRAINT [PK_DimAUS_SubCity] PRIMARY KEY CLUSTERED 	
(	
	[DimAUS_SubCityKey] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]	
) ON [PRIMARY]	


CREATE TABLE [dbo].[FactProperty](	
	[FactPropertyKey] [int] IDENTITY(1,1) NOT NULL,
	[SchoolKey] [int] NULL,
	[StationKey] [int] NULL,
	[SuburbKey] [int] NULL,
	[PropertyKey] [int] NULL,
 CONSTRAINT [PK_FactProperty] PRIMARY KEY CLUSTERED 	
(	
	[FactPropertyKey] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]	
) ON [PRIMARY]	



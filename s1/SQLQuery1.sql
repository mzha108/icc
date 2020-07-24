/* a. Display a list of all property names and their property id’s for Owner Id: 1426. */
select Property.Name as PropertyName, Property.Id as PropertyID
from Property inner join OwnerProperty
on OwnerProperty.OwnerId = '1426' and Property.id = OwnerProperty.PropertyId



/* b. Display the current home value for each property in question a). */
select Property.Name as PropertyName, Property.Id as PropertyID, sum(PropertyHomeValue.Value) as Value
from Property inner join OwnerProperty
on OwnerProperty.OwnerId = '1426' and Property.id = OwnerProperty.PropertyId
inner join PropertyHomeValue
on PropertyHomeValue.PropertyId = Property.id
group by Property.Name, Property.Id


/* c. For each property in question a), return the following: */
/* i. Using rental payment amount, rental payment frequency, tenant start date and tenant end date to write a query that returns the sum of all payments from start date to end date. */
select tbl2.OwnerID, tbl2.PropertyID, tbl2.PropertyName, tbl1.PaymentAmount*tbl1.NumberOfPayment as TotalPayment, tbl1.StartDate, 
	   tbl1.EndDate, tbl1.NumberOfPayment, tbl1.PaymentAmount, tbl1.PaymentFrequencyId, TenantPaymentFrequencies.Code as PaymentFrequencyCode
from
	(select 
		case
			when t.PaymentFrequencyId=1 then DATEDIFF(week, t.StartDate, isnull(t.EndDate, getdate()))
			when t.PaymentFrequencyId=2 then DATEDIFF(week, t.StartDate, isnull(t.EndDate, getdate())) / 2
			else DATEDIFF(MONTH, t.startdate, isnull(t.enddate, getdate()))
		end as NumberOfPayment, startdate, enddate, PropertyId, PaymentAmount, PaymentFrequencyId
	from TenantProperty t
	) as tbl1, 
	(select Property.Name as PropertyName, Property.Id as PropertyID, OwnerProperty.OwnerId as OwnerID
	from Property inner join OwnerProperty
	on OwnerProperty.OwnerId = '1426' and Property.id = OwnerProperty.PropertyId) as tbl2,
	TenantPaymentFrequencies
where tbl1.PropertyId = tbl2.PropertyID and TenantPaymentFrequencies.Id = tbl1.PaymentFrequencyId

/* ii. Display the yield. */
select *
from
	(select Property.Name as PropertyName, Property.Id as PropertyID
	from Property inner join OwnerProperty
	on OwnerProperty.OwnerId = '1426' and Property.id = OwnerProperty.PropertyId
	) as tbl1, PropertyFinance as tbl2
where tbl1.PropertyID = tbl2.PropertyId



/* d. Display all the jobs available */
select Job.Id, Job.JobDescription, Job.JobStartDate, job.JobEndDate, job.JobStatusId, 
	   job.OwnerId, job.PropertyId, JobMedia.IsActive from Job, JobMedia
where JobMedia.JobId = Job.Id and JobMedia.IsActive = '1'

/* e. Display all property names, current tenants first and last names and rental payments per week/fortnight/month for the properties in question a). */
select pr.Name, p.FirstName, p.LastName, tbl1.*, tpf.Code
from
	(select 
		case
			when t.PaymentFrequencyId=1 then DATEDIFF(week, t.StartDate, isnull(t.EndDate, getdate()))
			when t.PaymentFrequencyId=2 then DATEDIFF(week, t.StartDate, isnull(t.EndDate, getdate())) / 2
			else DATEDIFF(MONTH, t.startdate, isnull(t.enddate, getdate()))
		end as NumberOfPayment, TenantId, startdate, enddate, PropertyId, PaymentAmount, PaymentFrequencyId
	from TenantProperty t, Tenant 
	where t.IsActive = '1' and Tenant.Id = t.TenantId) as tbl1, Person p, Property pr, TenantPaymentFrequencies tpf,

	(select Property.Name as PropertyName, Property.Id as PropertyID, OwnerProperty.OwnerId as OwnerID
	from Property inner join OwnerProperty
	on OwnerProperty.OwnerId = '1426' and Property.id = OwnerProperty.PropertyId) as tbl2

where tbl1.TenantId = p.Id and tbl1.PropertyId = pr.Id and tbl1.PropertyId = tbl2.PropertyID and tbl1.PaymentFrequencyId = tpf.Id 

order by tbl1.PaymentFrequencyId desc

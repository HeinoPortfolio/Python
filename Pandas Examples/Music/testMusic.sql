SELECT customer.LastName, customer.FirstName, track.Name , album.Title
FROM Customer
JOIN invoice ON customer.CustomerId = invoice.CustomerId
JOIN invoiceline ON invoice.InvoiceId = invoiceline.InvoiceId
JOIN track ON invoiceline.TrackId = track.TrackId
JOIN album ON track.AlbumId = album.AlbumId
ORDER BY customer.LastName;









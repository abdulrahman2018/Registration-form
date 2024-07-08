using Microsoft.EntityFrameworkCore;
using RegistrationFormApp.Models;

namespace RegistrationFormApp.Data
{
    public class AppDbContext : DbContext
    {
        public AppDbContext(DbContextOptions<AppDbContext> options) : base(options) { }

        public DbSet<Registration> Registrations { get; set; }
    }
}

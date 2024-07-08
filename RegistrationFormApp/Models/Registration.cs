namespace RegistrationFormApp.Models
{
    public class Registration
    {
        public int Id { get; set; }
        public required string Name { get; set; }
        public required string Email { get; set; }
        public required string Phone { get; set; }
        public int Age { get; set; }
    }
}

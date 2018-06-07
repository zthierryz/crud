from django.db import models

civilites_liste = (
    ('Mme', 'Mme'),
    ('M', 'M'),
)


class Membre(models.Model):
    civilite = models.CharField(max_length=5, null=True, blank=True, choices=civilites_liste)
    nom = models.CharField(max_length=100,)
    prenom = models.CharField(max_length=100, null=True, blank=True)
    date_de_naissance = models.DateField(null=True, blank=True)
    cree_le = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return('{0} {1}'.format(self.prenom, self.nom))

    class Meta:
        ordering = ('nom', 'prenom')
        unique_together = ('nom', 'prenom', 'date_de_naissance')


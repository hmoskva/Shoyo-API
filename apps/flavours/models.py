from django.db import models


class Flavour(models.Model):
    """Model definition for Flavour."""

    name = models.CharField(max_length=256)
    image = models.URLField(max_length=256, null=True, blank=True)

    class Meta:
        """Meta definition for Flavour."""

        verbose_name = 'Flavour'
        verbose_name_plural = 'Flavours'

    def __str__(self):
        """Unicode representation of Flavour."""
        return self.name

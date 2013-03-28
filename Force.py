import numpy as np
import math


class Force(object):

    def __init__(self, c):
        self.c = c

    def pe(self):
        eps = 1.
        sig = 1.

        dx = self.c.dx()
        dy = self.c.dy()
        dz = self.c.dz()
        dr2 = self.c.dr2()

        r_mag = np.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
        r_mag = np.nan_to_num(r_mag)

        rgBuild = 4. * eps * ((sig / r_mag) ** 12 - (sig / r_mag) ** 6)
        #rgBuild = (4 * eps) * ((2 * (sig**12 / r_mag**6)) - (sig**6 / r_mag**3))
        rgBuild = np.nan_to_num(rgBuild)
        #print "rgBuild:"
        #print np.sum(rgBuild)
        #print "-------------------"
        return np.sum(rgBuild) / np.size(self.c.x)

    # TODO: ke calculation
    def ke(self):
        d = 2.
        N = np.size(self.c.x)
        vx = self.c.vx.copy()
        vy = self.c.vy.copy()
        vz = self.c.vz.copy()
        return 1 / ((N - 1) * d) * np.sum(vx ** 2 * vy ** 2)

    # TODO: pressure calculation
    def pressure(self):
        ps = 1.
        sig = 1.
        eps = 1.
        d = 2.
        N = np.size(self.c.x)

        dx = self.c.dx()
        dy = self.c.dy()
        dz = self.c.dz()
        dr2 = self.c.dr2()

        r_mag = (dx ** 2 + dy ** 2 + dz ** 2)
        r_mag = np.nan_to_num(r_mag)

        px = dx * (24 * eps / r_mag) * ((2 * (sig**12 / r_mag**6)) - (sig**6 / r_mag**3))
        px = np.nan_to_num(px)
        px = np.triu(px)
        py = dy * (24 * eps / r_mag) * ((2 * (sig**12 / r_mag**6)) - (sig**6 / r_mag**3))
        py = np.nan_to_num(py)
        py = np.triu(py)
        pz = dz * (24 * eps / r_mag) * ((2 * (sig**12 / r_mag**6)) - (sig**6 / r_mag**3))
        pz = np.nan_to_num(pz)
        pz = np.triu(pz)
        pt = px + py + pz
        return 1 / (d * N * self.ke()) * np.sum(pt)

    def ax(self):
        eps = 1.0
        sig = 1.0
        dx = self.c.dx()
        dy = self.c.dy()
        dz = self.c.dz()
        dr = self.c.dr()

        r_mag = np.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
        r_mag = np.nan_to_num(r_mag)
        x_hat = dx / r_mag
        x_hat = np.nan_to_num(x_hat)

        #print "r_mag"
        #print r_mag

        #print "x_hat"
        #print x_hat

        ax = ((24 * eps) / r_mag * (2 * (sig / r_mag) ** 12 - (sig / r_mag) ** 6)) * x_hat
        ax = np.nan_to_num(ax)

        ax = -ax
        #force = r_hat * (24*eps)/r_mag * (2*(sig/r_mag)**12 - (sig/r_mag)**6)
        #print "ax: "
        #print np.sum(ax, axis=1)
        return np.sum(ax, axis=1)

    def ay(self):
        eps = 1.0
        sig = 1.0
        dx = self.c.dx()
        dy = self.c.dy()
        dz = self.c.dz()
        dr = self.c.dr()

        r_mag = np.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
        r_mag = np.nan_to_num(r_mag)
        y_hat = dy / r_mag
        y_hat = np.nan_to_num(y_hat)

        #print "r_mag"
        #print r_mag

        #print "y_hat"
        #print y_hat

        ay = y_hat * ((24 * eps) / r_mag * (2 * (sig / r_mag) ** 12 - (sig / r_mag) ** 6))
        ay = np.nan_to_num(ay)

        ay = -ay

        #force = r_hat * (24*eps)/r_mag * (2*(sig/r_mag)**12 - (sig/r_mag)**6)
        #print "ay: "
        #print np.sum(ay, axis=1)
        return np.sum(ay, axis=1)

    def az(self):
        eps = 1.0
        sig = 1.0
        dx = self.c.dx()
        dy = self.c.dy()
        dz = self.c.dz()
        dr = self.c.dr()

        r_mag = np.sqrt(dx ** 2 + dy ** 2 + dz ** 2)
        r_mag = np.nan_to_num(r_mag)
        z_hat = dz / r_mag
        z_hat = np.nan_to_num(z_hat)

        #print "r_mag"
        #print r_mag

        #print "z_hat"
        #print z_hat

        az = z_hat * ((24 * eps) / r_mag * (2 * (sig / r_mag) ** 12 - (sig / r_mag) ** 6))
        az = np.nan_to_num(az)

        az = -az
        #force = r_hat * (24*eps)/r_mag * (2*(sig/r_mag)**12 - (sig/r_mag)**6)
        #print "az: "
        #print np.sum(az, axis=1)
        return np.sum(az, axis=1)

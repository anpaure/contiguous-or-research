# Mountain predecessor renewal with positive terminal occupancy: exact winding, susceptibility, and the short-cycle no-go

Date: 2026-07-26

Method: pure mathematics only. No computation, finite search, solver, or
external input is used.

## 0. Outcome

Let

\[
 q\ge1,\qquad h=q+1,\qquad p=2q+1=2h-1,
\]

and let the parent semilength be

\[
 r=h+y\quad (y\ge1),\qquad N=2r+1.
\]

The complete inverse peak-deletion fibre over the mountain
\(M_q=1^q0^q\) is

\[
 \Omega_{y,p}=\left\{\mathbf n=(n_0,\ldots,n_{p-1})\in
 \mathbb Z_{\ge0}^{p}:\sum_i n_i=y\right\}.
 \tag{0.1}
\]

The PBBS quotient map rotates these coordinates by one place.  This note
extends the terminal-zero calculation to every terminal value \(n_0=z\).
The extension is exact:

\[
 \boxed{G(\mathbf n)=g_z:=2+(2z+1)p,\qquad
        s_z:={g_z-1\over2}=h+zp,\qquad
        w(\mathbf n)=z,}                         \tag{0.2}
\]

whenever \(g_z<N\).  Here \(G\) is the first physical-coordinate return
gap, \(s_z\) is its step-two duration, and \(w\) is its winding number.
Thus terminal occupancy is literally winding in this rotor; positive
terminal occupancy is not merely correlated with positive winding.

For an ST cutoff \(G_H=2H-1<N\), put

\[
 Z_H=\min\left\{y,
 \left\lfloor{2H-3-p\over2p}\right\rfloor\right\},             \tag{0.3}
\]

with the convention that the active set is empty when the displayed
floor is negative.  Then the complete mountain-fibre active set is

\[
 \boxed{E_H^{\rm mt}=\{\mathbf n:n_0\le Z_H\},\qquad
        E_H^{{\rm mt},+}=\{\mathbf n:1\le n_0\le Z_H\}.}       \tag{0.4}
\]

For any set \(S\subseteq\{0,1,\ldots,y\}\), let \(E_S=\{n_0\in S\}\),
and use the convention \(\binom ab=0\) outside its natural range.  Define

\[
 R_S=\sum_{a\in S}\binom{y-a+p-2}{p-2},                       \tag{0.5}
\]

\[
 J_S=\sum_{a,b\in S}\binom{y-a-b+p-3}{p-3}.                  \tag{0.6}
\]

For every integer \(L\ge1\), the exact two-point susceptibility on the
whole fibre is

\[
 \boxed{
 \mathcal C_S(L):=\sum_{t=1}^{L}|E_S\cap\tau^{-t}E_S|
 =\left\lfloor{L\over p}\right\rfloor R_S+
 \left(L-\left\lfloor{L\over p}\right\rfloor\right)J_S.}     \tag{0.7}
\]

In particular all fixed finite winding windows have bounded
susceptibility on the Gaussian scale.  If

\[
 {h\over\sqrt r}\longrightarrow c>0,
 \qquad {H\over\sqrt r}\longrightarrow A>0,                  \tag{0.8}
\]

and \(S\) is a fixed nonempty finite set, then

\[
 H{R_S\over|\Omega_{y,p}|}\longrightarrow2Ac|S|              \tag{0.9}
\]

and, with \(L=H+1\),

\[
 \boxed{{\mathcal C_S(H+1)\over R_S}
 =\left\lfloor{H+1\over p}\right\rfloor+2Ac|S|+o(1).}       \tag{0.10}
\]

Formula (0.10), rather than a local marginal, is the exact cyclic renewal
calculation, including the deterministic returns of the state after each
full rotor lap.

However, the positive-winding branch is completely removed by the ST
long-cycle truncation.  Indeed, if even one \(z\ge1\) is active, then

\[
 3p+2\le g_z\le2H-1,
 \qquad	ext{hence}\qquad
 p\le{2H-3\over3}<H+1.                           \tag{0.11}
\]

Every quotient orbit in \(\Omega_{y,p}\) has period dividing \(p\).
Thus every positive-winding mountain-fibre start lies on a quotient cycle
of length at most \(H+1\), and none belongs to the retained set \(E_H\).
There is a sharp dichotomy:

* a mountain rotor can have retained terminal-zero starts by taking
  \(p>H+1\), but then no terminal value \(z\ge1\) is active;
* if a positive terminal value is active, the entire rotor is a deleted
  short-cycle sector.

Finally, a long-period spectator cannot be attached in the same inverse
generation.  The weak-composition parametrization (0.1) is exhaustive:
every decoration erased by one simultaneous peak deletion and leaving
the core \(M_q\) is one of its coordinates, and \(\tau^p\) is the identity
on the complete fibre.  Consequently no peak-level spectator can increase
the quotient period beyond \(p\) while preserving the mountain core and
the return law (0.2).  A viable long-period extension must change the
first-pruned core (or use at least one further inverse generation), at
which point the arithmetic predecessor itinerary used in (0.2) is no
longer inherited automatically.  Whether such a genuinely deeper
extension can preserve (0.2) is not proved here.

The bounded ratios in (0.10) therefore do not refute \((ST_A)\): the
positive part has zero retained mass, while the retained zero part is
Catalan-negligible.  The theorem instead closes the most direct
positive-winding mountain extension and identifies precisely what a
long-period construction would have to evade.

## 1. Exact predecessor passage

The mountain equality-particle itinerary has period \(p\).  If \(a\) is
the time-zero selected particle and \(b=a-1\) its immediate predecessor,
then the positive selection times of \(b\) are

\[
 T_j=2+(j-1)p\qquad(j\ge1).                       \tag{1.1}
\]

In the inverse lift, terminal occupancy \(n_0=z\) makes the lifted
distance from \(b\) to the returned edge equal to \(2z+1\).  The exact
terminal-spacing theorem therefore requires the \((2z+2)\)-nd positive
selection of \(b\), and gives

\[
 G(\mathbf n)=T_{2z+2}=2+(2z+1)p.                \tag{1.2}
\]

If (1.2) is below \(N\), the distinguished particle cannot make a full
physical circuit before this time, equality particles cannot overtake,
and the terminal-spacing theorem proves that this is the first repeated
physical coordinate.  This proves the first two assertions of (0.2).

The cutoff condition \(g_z\le2H-1\) is exactly

\[
 z\le {2H-3-p\over2p},                            \tag{1.3}
\]

which proves (0.3)--(0.4).

## 2. Exact winding audit

The mountain-fibre rotation and endpoint formulas give

\[
 d(\mathbf n)=1+2n_0,                             \tag{2.1}
\]

and

\[
 \sum_{j=0}^{h-1}d(\tau^j\mathbf n)
 -\delta(\tau^h\mathbf n)=2n_0=2z.              \tag{2.2}
\]

One complete rotor lap has deficit

\[
 \sum_{j=0}^{p-1}d(\tau^j\mathbf n)
 =p+2\sum_i n_i
 =2h-1+2(r-h)
 =2r-1=N-2.                                      \tag{2.3}
\]

Since \(s_z=h+zp\) and \(\tau^{zp}\mathbf n=\mathbf n\), equations
(2.2)--(2.3) give

\[
\begin{aligned}
 \sum_{j=0}^{s_z-1}d(\tau^j\mathbf n)
  -\delta(\tau^{s_z}\mathbf n)
 &=z(N-2)+2z\\
 &=zN.                                            \tag{2.4}
\end{aligned}
\]

The integer multiplying \(N\) in the exact return ledger is the winding
number.  Therefore \(w=z\), proving the last assertion of (0.2).  Notice
that this argument includes every positive winding and uses neither a
zero-winding converse nor a reduced-height surrogate.

## 3. Exact two-point transfer

Stars and bars gives

\[
 |\Omega_{y,p}|=\binom{y+p-1}{p-1}.              \tag{3.1}
\]

Fixing \(n_0=a\) leaves \(p-1\) coordinates with mass \(y-a\), which
proves (0.5).  If \(t\not\equiv0\pmod p\), the conditions at phases zero
and \(t\) address two distinct coordinates.  Fixing their values to
\(a,b\) leaves \(p-2\) coordinates with mass \(y-a-b\), and hence

\[
 |E_S\cap\tau^{-t}E_S|=J_S.                      \tag{3.2}
\]

If \(t\equiv0\pmod p\), then \(\tau^t\) is the identity on the entire
fibre, so the same intersection equals \(R_S\).  Among
\(1,\ldots,L\), exactly \(\lfloor L/p\rfloor\) lags are multiples of
\(p\).  Summing proves (0.7).  This remains valid when individual vectors
have a proper divisor of \(p\) as their orbit period; such extra
self-overlaps are already counted correctly inside (3.2).

For completeness, if \(S\) is fixed while (0.8) holds, then uniformly for
\(a,b\in S\),

\[
 {\binom{y-a+p-2}{p-2}\over\binom{y+p-1}{p-1}}
 =(1+o(1)){p\over y},                             \tag{3.3}
\]

\[
 {\binom{y-a-b+p-3}{p-3}\over\binom{y+p-1}{p-1}}
 =(1+o(1))\left({p\over y}\right)^2.             \tag{3.4}
\]

Since \(p/\sqrt r\to2c\), \(y/r\to1\), and
\(H/\sqrt r\to A\), equations (3.3)--(3.4) imply

\[
 {R_S\over|\Omega_{y,p}|}
 =(1+o(1))|S|{p\over y},
 \qquad
 {J_S\over R_S}
 =(1+o(1))|S|{p\over y}.                         \tag{3.5}
\]

Substitution in (0.7) proves (0.9)--(0.10).  At a boundary where
\((H+1)/p\) tends to an integer, the floor in (0.10) must be retained;
the formula is exact and no hidden subsequence convention is being used.

If the active winding set stabilizes away from a cutoff boundary, write

\[
 Z_*=\max\{z\ge0:(2z+1)c<A\}.                    \tag{3.6}
\]

Then (0.9)--(0.10) apply to all active windings with
\(S=\{0,\ldots,Z_*\}\), and to the positive part with
\(S=\{1,\ldots,Z_*\}\).  In the latter case \(|S|=Z_*\).

## 4. Short-cycle exclusion and the spectator boundary

The rotation theorem gives

\[
                         \tau^p=\mathrm{id}
 \quad\hbox{on }\Omega_{y,p}.                    \tag{4.1}
\]

If \(z\ge1\) is active, then its first return is no earlier than
\(g_1=3p+2\).  The cutoff gives (0.11).  Thus its quotient orbit has
length dividing \(p<H+1\), whereas the retained ST deck contains only
cycles of length greater than \(H+1\).  This proves exact exclusion, not
an asymptotic estimate.

Now consider a proposed spectator that is erased together with the other
new peaks and leaves \(M_q\) after one simultaneous peak deletion.  The
inverse peak-deletion theorem says that every such word occurs exactly
once in (0.1): all erased material is distributed among the \(p\) ordered
leaf slots.  By (4.1), every one of these states has quotient period at
most \(p\), independently of the amount or placement of free mass.
Therefore such a spectator cannot make an active positive-winding state
survive the long-cycle deletion.

A spectator containing an edge that survives the first deletion changes
the first-pruned core.  The exact return criterion then reads

\[
 G(D)=T_{2z+2}(\partial D),                       \tag{4.2}
\]

where the predecessor times are those of the new core, not those of
\(M_q\).  Nothing in peak-deletion commutation identifies these times with
the arithmetic progression (1.1).  Hence a deeper spectator is a genuine
new dynamical construction, not an extension of the mountain rotor by a
free factor.  This note neither constructs nor excludes such a new core.

## 5. Implication boundary

The proved statements are:

1. the exact active terminal layers for the complete mountain fibre;
2. exact equality of terminal occupancy and winding;
3. the full cyclic two-point transfer, with all positive windings;
4. bounded Gaussian-scale susceptibility for every fixed winding window;
5. exact exclusion of every active positive-winding layer by the
   long-cycle truncation; and
6. impossibility of a one-generation, deletion-preserving long-period
   spectator.

They do not give a global Catalan-scale counterexample to \((ST_A)\), nor
do they exclude a multi-generation construction whose first-pruned core
has long period and happens to reproduce the same predecessor passage.
The precise remaining mountain-inspired problem is therefore to construct
or rule out a long-period reduced core \(F\) for which a positive-density
family of phases has the arithmetic local passage law
\(T_j(F)=2+(j-1)p\) through \(j=2Z+2\).  The original mountain core cannot
provide it after the retained-cycle deletion.

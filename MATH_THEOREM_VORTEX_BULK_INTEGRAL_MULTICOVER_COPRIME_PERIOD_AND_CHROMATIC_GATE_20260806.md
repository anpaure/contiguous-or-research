# The unchanged vortex bulk has an exact integral packet multicover

## Status

This note proves an integral statement on the completely unchanged side of
the balanced-vortex halo.  It is stronger than fractional feasibility but
weaker than the desired one-copy packet factor.

Delete every `D+2` two-hole packet which contains an owner in a prescribed
balanced slice.  On every source-width row, every target outside the exact
rectangular exposure halo retains its full packet degree.  Taking every
surviving packet once therefore gives an **exact integral regular
multicover** of the unchanged bulk.  Moreover all rows can be marked down to
one common multiplicity, namely the owner degree `D_0`.

There is also no residual scalar divisibility obstruction once the two
consecutive periods `D+2` and `D+3` are admitted.  Every sufficiently large
resource count is a nonnegative combination of these periods, using fewer
than `D+2` packets of the second period.  Their entire immediate-resource
footprint is `O(D^2)=O(r)`, and even their fully exposed proper-window
footprint is `O(D^3)=O(r^(3/2))`; both are negligible compared with a
critical balanced-vortex halo.

What is **not** proved is that the regular multicover splits into
`D_0+o(D_0 |H|/W)` matchings, or that one colour is simultaneously
pseudorandom on all marked rows.  An exact edge-colouring reduction below
identifies this as the remaining bulk-rounding theorem.  Thus this note
does not claim a one-copy cover-down.

## 1. Two-hole packets and all source-width rows

Put

\[
 n=2r-1,\qquad D=d+1,\qquad L=D+2,\qquad c=r-D.          \tag{1.1}
\]

A two-hole packet is specified by

\[
 K\subset H\subset[n],\qquad |K|=c,\quad |H|=r+2,
 \quad F=H-K,\quad |F|=L,                                \tag{1.2}
\]

and a cyclic order `(f_t)_(t in Z_L)` of `F`.  Its source word is

\[
                              A_t=K\cup\{f_t\}.           \tag{1.3}
\]

For `1<=q<=D+1`, let

\[
 V_{t,q}=K\cup\{f_t,f_{t+1},\ldots,f_{t+q-1}\}.         \tag{1.4}
\]

The rows `q=D-1,D,D+1` are respectively the immediate-lower roots,
owners, and immediate-upper colours.  Every row in (1.4) is simple inside
one packet, since a proper cyclic interval of distinct labels recovers its
start.

Let

\[
                 W=\binom nr
\]

and let `D_0` be the common full packet degree of one owner and one root.
The full number of packets is

\[
                         |\mathcal P|={WD_0\over L}.      \tag{1.5}
\]

### Lemma 1.1 (exact degree of every width row)

Every rank-`(c+q)` target has packet-occurrence degree

\[
 \boxed{
 E_q={WD_0\over\binom n{c+q}}.}                          \tag{1.6}
\]

In particular,

\[
 E_{D-1}=E_D=D_0,\qquad
 E_{D+1}=D_0{r+1\over r-1},qquad E_q\ge D_0.             \tag{1.7}
\]

#### Proof

There are `|P|L=WD_0` row-`q` occurrences.  The symmetric group is
transitive on the rank-`(c+q)` targets, so double counting gives (1.6).
The two central ranks of the odd Boolean lattice both have size `W`, and
every other rank occurring here has size at most `W`.  This proves
(1.7).  \(\square\)

## 2. Exact unchanged-row halo

Fix disjoint coordinate banks `A,B` with `|A|=|B|=a`, and put

\[
 \alpha(X)=|A-X|,\qquad \beta(X)=|B\cap X|.              \tag{2.1}
\]

The balanced owner slice is

\[
 \mathcal S=\{X\in\tbinom{[n]}r:A\subseteq X,
                                  X\cap B=\varnothing\}. \tag{2.2}
\]

Let `P^circ` be the family of all two-hole packets containing no owner of
`S`.

For row `q`, define its unchanged bulk by

\[
 \mathcal B_q=
 \left\{X\in\tbinom{[n]}{c+q}:
       \alpha(X)>L-q\ \hbox{ or }\ \beta(X)>2\right\}.   \tag{2.3}
\]

Thus the deleted rectangular halo is

\[
       \alpha\le L-q,\qquad\beta\le2.                    \tag{2.4}
\]

At `q=D-1,D,D+1`, (2.4) gives exactly the root, owner, and upper
rectangles `(3,2),(2,2),(1,2)` from the balanced-coordinate exposure
theorem.

### Theorem 2.1 (all-width literal degree preservation)

For every `1<=q<=D+1` and every `X in B_q`, every packet occurrence of
`X` belongs to `P^circ`.  Consequently

\[
                 d_{\mathcal P^\circ}(X)=E_q.            \tag{2.5}
\]

#### Proof

Suppose a packet contains a slice owner.  In hole notation this owner is
`H-e_*`, where `e_*` is one cyclic two-interval.  Slice membership gives

\[
                  A\subseteq H,\qquad
                  H\cap B\subseteq e_*,\qquad
                  A\cap e_*=\varnothing.                 \tag{2.6}
\]

A row-`q` occurrence is `H-J`, where `J` is the complementary cyclic
interval of length `L-q`.  Since `A subset H`, it can omit at most
`L-q` members of `A`.  Since every member of `B` which lies in `H` is
already in the two-set `e_*`, it can contain at most two members of `B`.
Thus every row-`q` occurrence of a slice-hitting packet lies in (2.4).
The contrapositive proves the first assertion, and no incident packet of a
bulk target was deleted.  Lemma 1.1 gives (2.5).  \(\square\)

This also shows why a fixed radius-three halo controls only the three
central rows.  A low source-width target has the larger, exact aperture
`L-q`; claiming radius three for all lower tickets would be false.

## 3. Exact integral regular multicover

### Theorem 3.1 (zero-defect integral bulk multicover)

Take every packet of `P^circ` exactly once.  Then, simultaneously for all
`1<=q<=D+1`, every target in `B_q` is covered exactly `E_q` times.

Furthermore, one may mark occurrences so that every target in every
`B_q` has exactly `D_0` marked providers.  Hence the same integral packet
family is a common `D_0`-fold marked cover of every unchanged row.  On the
owner and root rows every occurrence is already marked.

#### Proof

The first assertion is just (2.5), interpreted integrally: the packet
family is a set, not a fractional weighting, and each packet is taken once.
By (1.7), `E_q>=D_0`.  For each target independently choose any `D_0` of
its `E_q` incident occurrences and mark them.  A row occurrence has one
well-defined target, so these choices do not compete.  At `q=D-1,D`,
`E_q=D_0`, forcing every occurrence to be marked.  \(\square\)

The theorem has no uncovered bulk target at all.  Its limitation is
multiplicity: different selected packets share resources.  It is therefore
an exact integral **cover**, not a matching or chronology.

## 4. The exact chromatic reduction to one-copy cover-down

Make a hypergraph `G` whose edges are the packets in `P^circ` and whose
vertices are **all** owner and root resources used by those packets,
including halo resources.  Thus a colour class of a proper edge-colouring
of `G` is a genuine owner/root packet matching.  Every vertex has degree at
most `D_0`, and every bulk owner/root vertex has degree exactly `D_0`.

Let

\[
 N_{\rm bulk}=|\mathcal B_D|+|\mathcal B_{D-1}|.          \tag{4.1}
\]

### Theorem 4.1 (near-`D_0` edge colouring implies vortex cover-down)

If

\[
                       \chi'(G)\le D_0+t,                \tag{4.2}
\]

then `G` contains a packet matching leaving at most

\[
 \boxed{
       N_{\rm bulk}{t\over D_0+t}}                       \tag{4.3}
\]

bulk owner/root resources uncovered.

In particular, if `H` denotes the owner/root radius-three halo and

\[
                        {t\over D_0}=o(|H|/W),            \tag{4.4}
\]

then the leave is `o(|H|)`.

#### Proof

Across all colours, every bulk vertex is covered in exactly `D_0` colour
classes.  Hence the sum, over the `D_0+t` colours, of their bulk coverage
is `D_0 N_bulk`.  Some colour covers at least the average
`D_0 N_bulk/(D_0+t)`.  Its complement has size at most (4.3).  Equation
(4.4) gives the final assertion.  \(\square\)

For the critical choice `a=(1/4)log_2 r+O(1)`, the root halo is the largest
of the central three and

\[
                         |H|/W=\Theta(4^{-a}a^5)
                              =\Theta(a^5/\sqrt r).       \tag{4.5}
\]

Thus the required relative edge-colouring error is only
`o(a^5/sqrt(r))`.  The exact pair and aggregate-codegree ledgers make this
plausible, but no presently proved growing-uniformity edge-colouring theorem
in the project supplies (4.2)--(4.4).  Theorem 4.1 is a reduction, not an
invocation of such a theorem.

For completeness, the lower bound in (4.5) comes from the single root-halo
summand `alpha=3,beta=2` in the exact halo formula; its neutral binomial
coefficient is within a constant factor of the central one when
`a=o(sqrt r)`.  The matching upper bound is the finite sum over
`alpha<=3,beta<=2`.

One can form an expanded marked hypergraph by adjoining the marked
providers from Theorem 3.1 to each packet edge.  It still has maximum
degree `D_0`, and a proper colour is then collision-free on every marked
row.  Its edge rank is `O(DL)=O(r)`, however, and an edge-colouring with the
error in (4.4) is an even stronger unproved statement.  This is the exact
point at which upper providers and complete chain tickets cease to be
automatic.

## 5. Consecutive periods remove scalar divisibility

The preceding two-hole period is only the first member of a simple family.
Let `2<=b<=r-1`, assume `D>=2`, and put

\[
 L_b=D+b,qquad |K|=c,qquad |F|=L_b,qquad H=K\cup F,
 \quad |H|=r+b.                                          \tag{5.1}
\]

Use again the cyclic source `K union {f_t}`.  Its central resources are

\[
 \begin{aligned}
 O_t&=H-I_b(t),\\
 Q_t&=H-I_{b+1}(t),\\
 U_t&=H-I_{b-1}(t+1),
 \end{aligned}                                           \tag{5.2}
\]

where `I_j(t)` is a cyclic `j`-interval.  They have ranks `r,r-1,r+1`,
and all three rows are simple.

### Lemma 5.1 (general hole exposure)

If a period-`L_b` packet contains a slice owner, then every resource in
(5.2) satisfies

\[
 \begin{array}{c|cc}
      &\alpha&\beta\\ \hline
 O&\le b&\le b\\
 Q&\le b+1&\le b\\
 U&\le b-1&\le b.
 \end{array}                                             \tag{5.3}
\]

More generally its width-`q` source unions satisfy

\[
                         \alpha\le L_b-q,
                    \qquad\beta\le b.                   \tag{5.4}
\]

#### Proof

If the slice owner is `H-I_b^*`, then `A subset H`,
`H cap B subset I_b^*`, and `A cap I_b^*` is empty.  A resource whose
complementary hole has size `j` can omit at most `j` members of `A`, while
all its surviving `B`-coordinates lie in the `b`-set `I_b^*`.  Substitute
`j=b,b+1,b-1,L_b-q`.  \(\square\)

### Theorem 5.2 (coprime-period scalar completion)

Let

\[
                         L_2=D+2,\qquad L_3=D+3.          \tag{5.5}
\]

Every integer

\[
                         N\ge(L_2-1)L_3                  \tag{5.6}
\]

has a representation

\[
                         N=xL_2+yL_3,qquad x,y\ge0,      \tag{5.7}
\]

with

\[
                              0\le y<L_2.                \tag{5.8}
\]

Thus a scalar owner/root ledger can always be made exact using only
`O(D)` period-`D+3` correction packets.  Their total owner/root/upper
footprint is `O(D^2)=O(r)`.  Exposing every proper source-width occurrence
raises this only to `O(D^3)=O(r^(3/2))`.

#### Proof

Since `L_3 congruent 1 (mod L_2)`, choose `y` to be the residue of `N`
modulo `L_2`, with `0<=y<L_2`, and put

\[
                         x={N-yL_3\over L_2}.             \tag{5.9}
\]

The numerator is divisible by `L_2` and is nonnegative by (5.6).  This
proves (5.7)--(5.8).  Each packet has `Theta(D)` resources in each central
row and `Theta(D^2)` occurrences across all proper widths.  Multiply by
`y=O(D)`.  Finally `D=Theta(sqrt r)`.  \(\square\)

At a critical balanced vortex the halo has exponential size
`Theta(W 4^{-a} poly(a))`, so both polynomial correction footprints in
Theorem 5.2 are `o(|H|)`.  Lemma 5.1 says exactly which slightly enlarged
coordinate halo contains those corrections.  Hence fixed-period
divisibility is not a genuine asymptotic obstruction.

Theorem 5.2 is deliberately scalar: it does not assert that the required
`D+3` packets can be planted resource-disjointly around an arbitrary
partial matching.  That planting is part of the integral cover-down gate.

## 6. Exact frontier

The rigorous bulk picture is now:

1. deleting all slice-hitting packets changes no incidence at all outside
   the row-dependent halo (2.4);
2. the surviving packets give a zero-defect integral regular multicover of
   every unchanged row, with one common marked multiplicity `D_0`;
3. the scalar congruence of a one-copy factor is removable with consecutive
   periods at polynomial, hence `o(halo)`, footprint;
4. obtaining one packet matching with `o(halo)` leave is exactly a
   near-`D_0` edge-colouring/pseudorandom-colour problem for this regular
   multicover;
5. retaining upper providers and all chain tickets asks for the same
   statement in the expanded marked hypergraph.

Thus the bulk has no remaining fractional, orbit, marking, or divisibility
obstruction.  The unresolved theorem is genuinely integral: split the
regular multicover into almost `D_0` disjoint near-factors (or construct one
such near-factor directly) while retaining the marked-row balance.

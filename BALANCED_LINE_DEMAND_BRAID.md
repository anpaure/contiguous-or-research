# The balanced line-demand braid has a linear-depth copy obstruction

## 1. Verdict

Put

\[
 P_m=[0,m]^4,\qquad R=2m-1,
\]

and let (2\le q\le \lfloor m/3\rfloor).  This note audits the
**balanced line-demand braid** proposed in Sections 7--8 of
`COMPLEMENTARY_SEAM_RECTANGLE_TILING.md`.  The conclusion is negative for
that literal architecture.

The incidence graph really is very simple.  With the canonical balanced
choice it is a disjoint union of diagonal paths.  With independently
reversed odd baselines its only possible cycles, after degree control, are
elementary four-cycles, and their parity monodromy is explicit.  Cutting
those cycles costs only (O(m^2)) seam corners.

That is not the physical obstruction.  The physical obstruction occurs
already at one odd seam:

> Every odd balanced seam has one portal corner one step outside its
> preferred intact line and its other portal corner one step inside its
> preferred intact line.

The inside arm cannot use the distinguished intact occurrence of that
line.  Through depth (q), it forces a second occurrence of (q-1)
consecutive line points.  There are (Theta(m^2)) independent interior odd
seams.  Consequently every literal balanced-arm braid which also retains
all preferred complete-line intervals has

\[
             \Omega(qm^2)                                      \tag{1.1}
\]

repeated base-layer occurrences.  For (q=\Theta(m)), this is
(Theta(m^3)), not (O(m^2)) and not (o(m^3)).

This lower bound is sharp in order.  Keeping all preferred line segments
intact and adding the balanced portal blocks separately uses

\[
             |L_R|+O(m^2)+O(qm^2)                              \tag{1.2}
\]

letters, with a uniform constant bound on the multiplicity of every base
point.  Thus the minimal repair of the literal balanced catalogue is a
second copy of one long arm at every interior odd port, not merely one
repeated endpoint per demand component.

This does **not** rule out a different upper-band construction.  It rules
out the claimed near-once completion which simultaneously insists on the
balanced suffix--prefix arms and on intact preferred line witnesses.

## 2. Exactly which seams are demanded

Fix one of the four high/low coordinate orientations and write a tie-strip
target as

\[
 y=(m-A,a,m-B,b),\qquad
 \delta=A+B=a+b-s+1,qquad 1\le s\le q.              \tag{2.1}
\]

For (delta=2r), the balanced baseline is ((c,d)=(r,r)).  Such a seam is
demanded if and only if

\[
                 A+r\le m,\qquad B+r\le m.           \tag{2.2}
\]

Indeed, when (2.2) holds, (s=1) and (a=b=r) give a legal tie target.
Conversely every tie target has (a,b\ge r), so (2.2) is necessary.

For (delta=2r+1), a tie target first occurs at depth two.  When (q\ge2),
the seam is demanded if and only if

\[
                 A+r+1\le m,\qquad B+r+1\le m.       \tag{2.3}
\]

Sufficiency follows by taking (s=2) and (a=b=r+1); necessity again
follows from the balanced lower bounds.  Thus the demanded seam set is
independent of (q) once (q\ge2).  The depth only determines how long
the requested arms are.

The case (q=1) has no odd demand and none of the obstruction below.  It
is the genuinely linear-depth regime (q\ge2) which matters here.

## 3. The explicit demand graph

Let

\[
 X_{B,t}=\hbox{the physical \(\{1,2\}\)-line with }(x_3,x_4)=(m-B-1,t),
                                                                    \tag{3.1}
\]

and

\[
 Y_{A,t}=\hbox{the physical \(\{3,4\}\)-line with }(x_1,x_2)=(m-A-1,t).
                                                                    \tag{3.2}
\]

The vertices of the demand graph are the actually occurring (X)- and
(Y)-lines.  A demanded seam ((A,B)) is an edge between its two physical
lines.

For an even seam (A+B=2r), the edge is forced:

\[
                 E_{A,B}: X_{B,r}\;--\;Y_{A,r}.       \tag{3.3}
\]

For an odd seam \(A+B=2r+1\), write \(\varepsilon_{A,B}=0\) for the
canonical baseline \((r,r+1)\), and \(\varepsilon_{A,B}=1\) for the reversed
baseline ((r+1,r)).  Then

\[
 O_{A,B}=\begin{cases}
 X_{B,r+1}\;--\;Y_{A,r},&\varepsilon_{A,B}=0,\\
 X_{B,r}\;--\;Y_{A,r+1},&\varepsilon_{A,B}=1.
 \end{cases}                                           \tag{3.4}
\]

These formulas include the boundary qualification from the independent
audit: a formal neighboring even seam may fail (2.2), in which case the
corresponding line vertex is simply a path endpoint.

### Canonical components

Take \(\varepsilon=0\) on every odd seam.  An even edge \(E_{A,B}\) can meet
only

\[
                 O_{A-1,B}\quad\hbox{and}\quad O_{A,B+1}.            \tag{3.5}
\]

After passing through either odd edge, the next even label is respectively
(E_{A-1,B-1}) or (E_{A+1,B+1}).  Hence every component has the invariant

\[
 \kappa=\begin{cases}
 A-B,&E_{A,B},\\
 A-B+1,&O_{A,B}.
 \end{cases}                                           \tag{3.6}
\]

Along fixed \(\kappa\), the even labels are linearly ordered by \(A\) (or
\(B\)), and odd labels join consecutive even labels when both exist.
Therefore every canonical component is a path; isolated seam edges count
as one-edge paths.  In particular, the canonical catalogue has no cycle
monodromy at all.

The boundary components can be counted exactly.  Write \(m=3h+j\),
\(j\in\{0,1,2\}\).  Direct substitution in (2.2)--(2.3) shows that the
nonempty canonical values of \(\kappa\) are

\[
\begin{array}{c|c|c}
j&\hbox{canonical \(\kappa\)-range}&\hbox{number of paths}\\ \hline
0&-2h,-2h+2,\ldots,2h&2h+1,\\
1&-2h,-2h+2,\ldots,2h&2h+1,\\
2&-2h,-2h+2,\ldots,2h+2&2h+2.
\end{array}                                             \tag{3.7}
\]

For each displayed value, the legal labels form one consecutive interval
in the diagonal parameter, so there is exactly one component, not merely
at most one.  Hence there are \(O(m)\), rather than \(O(m^2)\), canonical
boundary paths and exactly twice as many path-end line vertices.

If all odd baselines are reversed, the same statement holds with

\[
 \kappa=A-B\quad(E_{A,B}),\qquad
 \kappa=A-B-1\quad(O_{A,B}).                           \tag{3.8}
\]

The reversed table is the image of (3.7) under
\(\kappa\mapsto-\kappa\).

### Arbitrary odd choices and degree control

At (X_{B,t}), besides the possible even seam, the two possible odd
requests are

\[
 O_{\,2t-1-B,B}\quad(\varepsilon=0),\qquad
 O_{\,2t+1-B,B}\quad(\varepsilon=1).                  \tag{3.9}
\]

At (Y_{A,t}), they are

\[
 O_{\,A,2t-1-A}\quad(\varepsilon=1),\qquad
 O_{\,A,2t+1-A}\quad(\varepsilon=0).                  \tag{3.10}
\]

Thus, at an interior line carrying its even seam, degree at most two is
equivalent to forbidding both displayed odd requests simultaneously.  In
particular, down each fixed-(B) odd column one may not change from
canonical to reversed as (A) increases by two, while along each fixed-
(A) odd row one may not change from reversed to canonical as (B)
increases by two.  This recovers, and makes exact, the degree-three warning
in the audit.

There is a convenient complete component description.  Contract every
demanded even edge.  For fixed (kappa=A-B), the contracted even vertices

\[
                 E_{A,B},E_{A+1,B+1},E_{A+2,B+2},\ldots              \tag{3.11}
\]

lie on a path.  Between (E_{A,B}) and (E_{A+1,B+1}) there are at most
two parallel odd bridges:

\[
 \begin{array}{c|c|c}
 \hbox{odd label}&\hbox{baseline needed}&\hbox{bridge}\ \kappa\\ \hline
 O_{A,B+1}&0&A-B,\\
 O_{A+1,B}&1&A-B.
 \end{array}                                           \tag{3.12}
\]

The underlying simple graph is therefore a subgraph of a path.  Under the
degree-two conditions, every component is a path or an isolated doubled
edge.  Before contraction, a doubled edge is the alternating four-cycle

\[
 E_{A,B},\ O_{A,B+1},\ E_{A+1,B+1},\ O_{A+1,B}.        \tag{3.13}
\]

No longer cycle is possible.

### Parity monodromy

The balanced-baseline sheet is the bit \(\varepsilon\).  For a demand cycle
define

\[
                         \mu(C)=\bigoplus_{O\in C}\varepsilon(O).     \tag{3.14}
\]

Every cycle (3.13) contains one canonical and one reversed odd bridge, so

\[
                              \mu(C)=1.                              \tag{3.15}
\]

This is the complete parity monodromy: paths acquire a sheet after one
initial choice, while every cycle returns on the opposite balanced sheet.
One cut per four-cycle is necessary and sufficient to remove this
incidence-level monodromy.  There are only (O(m^2)) possible cycles, so
this part really can be repaired with (O(m^2)) repeated seam corners.

The next section shows why that repair is nevertheless physically
insufficient.

## 4. Odd seams have an unavoidable inward port

Consider first an (X_{B,d})-line in the chosen high/low orientation.  Its
preferred segment begins at

\[
 p^X_j=(m+B-2d-j, d+j, m-B-1, d),\qquad j=0,1,\ldots .            \tag{4.1}
\]

Here (p^X_0) lies on the equality boundary
(min(x_1,x_2)=min(x_3,x_4)=d), and increasing (j) moves inward.

Likewise the preferred part of a (Y_{A,c})-line begins at

\[
 p^Y_j=(m-A-1, c, m+A-2c-j, c+j),\qquad j=0,1,\ldots .            \tag{4.2}
\]

Direct substitution in the balanced seam endpoints gives the following
exact table.

\[
\begin{array}{c|c|c}
\hbox{seam type}&X\hbox{-corner}&Y\hbox{-corner}\\ \hline
\delta=2r&p^X_0&p^Y_0\\
\delta=2r+1,\ \varepsilon=0&p^X_{-1}&p^Y_1\\
\delta=2r+1,\ \varepsilon=1&p^X_1&p^Y_{-1}.
\end{array}                                             \tag{4.3}
\]

Thus reversing an odd baseline merely swaps the inward defect from one
line direction to the other.  It never removes it.

For the canonical odd seam, the (Y)-arm is

\[
                       p^Y_1,p^Y_2,\ldots,                         \tag{4.4}
\]

and for the reversed odd seam, the (X)-arm is

\[
                       p^X_1,p^X_2,\ldots .                        \tag{4.5}
\]

At depth (q), the tie target with parameters

\[
 (u,v)=(1,q-2)\quad(\varepsilon=0),qquad
 (u,v)=(q-2,1)\quad(\varepsilon=1)                 \tag{4.6}
\]

is legal whenever the arm stays in the box.  Its inward side uses exactly

\[
                         p_1,p_2,\ldots,p_{q-1}.                    \tag{4.7}
\]

These (q-1) letters must occur consecutively with the other seam arm
adjacent on the (p_1)-side.

## 5. The word obstruction

We state the precise scope, because it is stronger than an incidence
count but weaker than a no-go theorem for every possible OR construction.

### Exact meaning of intact preferred witnesses

The no-go statement permits arbitrary global interleaving, arbitrary cuts
between different physical lines, either orientation of every line block,
and arbitrary odd-baseline choices.  Its only preservation hypothesis is
the following local one.

For every line in the interior subcatalogue used below, the preferred easy
depth-(q) target at the equality boundary retains its literal complete-line
witness.  Equivalently, the word contains, in one of the two orientations,

\[
                         p_0,p_1,\ldots,p_q.                         \tag{5.1}
\]

This is precisely the endpoint-equality case of (7.2) or (7.3): the fixed
opposite-pair minimum is (b), the target minimum is (a=b+q), and
(b=a-q).  We do not assume that the rest of the physical line is intact.

### Lemma 1 (inward-arm duplication)

Suppose a word contains a distinguished preferred easy block

\[
                         p_0,p_1,\ldots,p_q                         \tag{5.2}
\]

in one of its two monotone orientations.  Suppose also that a literal
balanced portal witness requires

\[
                         p_1,p_2,\ldots,p_{q-1}                     \tag{5.3}
\]

consecutively, with a point outside this physical line adjacent on the
(p_1)-side.  Then none of the distinguished occurrences in (5.2) can
serve (5.3).  The word needs a second occurrence of every point in (5.3).

#### Proof

In the preferred easy block, the neighbor of (p_1) on its outward side is
(p_0), in either global orientation.  In the portal block, that neighbor
must be the opposite seam corner, which is a different point and is not on
this line.  If one occurrence from (5.3) were taken from the easy block,
the distinct line points and consecutive monotone order force all the
overlapping occurrences to align with (5.2), eventually forcing the
portal neighbor of (p_1) to equal (p_0), a contradiction.  Hence the
whole string (5.3) uses occurrences distinct from those in (5.2).  This
allows every other part of the physical line to be cut or reordered.
\(\square\)

### Theorem 2 (quantitative obstruction)

Let

\[
                         t=\left\lfloor {m-q-1\over3}\right\rfloor. \tag{5.4}
\]

In one fixed high/low orientation there are at least

\[
                         N_*=t(t+1)                                \tag{5.5}
\]

demanded odd seams whose full depth-(q) arms are legal.  Every word which

1. retains the literal preferred depth-(q) complete-line witness (5.1)
   on every line in the subcatalogue, and
2. realizes the tie strip by the literal balanced arms (7.9)--(7.10),

has at least

\[
                         {N_*(q-1)\over2}                          \tag{5.6}
\]

repeated base-layer occurrences.

#### Proof

For each (1\le r\le t), take the interior labels

\[
                    A,B\ge1,\qquad A+B=2r+1.                      \tag{5.7}
\]

There are (2r) choices.  The definition of (t) gives
(3r+q+1\le m).  Therefore (2.3) holds and every coordinate needed by the
depth-(q) arms, under either odd baseline, remains in the box and in the
chosen high/low orientation.  Summing (2r) proves (5.5).

The same inequality (3r+q+1\le m) makes the boundary easy block
(p_0,\ldots,p_q) legal on the inward line.  By (4.3)--(4.7) and Lemma 1,
each of these odd seams forces (q-1)
second arm occurrences.  Within one line direction, the inward physical
line determines the odd seam label uniquely: a canonical inward
(Y_{A,r}) determines (A,r), hence (B=2r+1-A); a reversed inward
(X_{B,r}) determines (B,r), hence (A=2r+1-B).  Thus inward arms of the
same direction do not share a line.

The restrictions (A,B\ge1) are essential when the odd baseline may be
chosen arbitrarily.  At either extreme label ((2r+1,0)) or ((0,2r+1)),
one baseline choice puts the inward defect on a line whose formal (p_0)
lies outside the box.  That preferred segment starts at (p_1), so its
distinguished occurrence need not be separate from the portal occurrence.
The interior subcatalogue removes exactly this boundary escape; see
`BALANCED_LINE_DEMAND_BRAID_AUDIT.md`.

A physical base point lies on exactly one (X)-line and exactly one
(Y)-line.  Consequently it belongs to at most one forced inward arm of
each direction.  Every such arm-point requirement needs an occurrence
separate from its preferred easy-block occurrence.  Even if one extra
occurrence serves both a crossing (X)-requirement and a crossing
(Y)-requirement, it pays at most two requirements.  Dividing by two gives
(5.6).  \(\square\)

For (q\le m/3), we have (t=\Theta(m)), so (5.6) is
(Omega(qm^2)).  In particular, if (q=\lfloor\alpha m\rfloor) for fixed
(0<\alpha\le1/3), the cost is (Omega(m^3)).

For (q=2), the forced string is the singleton (p_1), and the same argument
says that this point must occur twice.  There is no odd demand at (q=1),
so neither the statement nor the conclusion is intended to include that
boundary case.

The proof is immune to path orientations, cycle cuts, and odd-baseline
choices: those operations decide **which** line direction carries the
inward defect, but every odd seam has exactly one.

## 6. Matching bounded-copy repair

There is a simple construction showing that the order in Theorem 2 is the
right one for this architecture.

1. For every physical (X)-line, output its complete preferred segment as
   one monotone block.  Do the same for every physical (Y)-line.  Assign
   strict min-comparison points to their unique preferred system and retain
   equality points in both.  The equality surface has (O(m^2)) points, so
   the resulting easy-line word has length
   
   \[
                         |L_R|+O(m^2).                              \tag{6.1}
   \]

   Every preferred witness from (7.2)--(7.3) is still an internal
   contiguous line interval.

2. Use the canonical baseline for every demanded seam.  For each of the
   four high/low orientations and each demanded label ((A,B)), append the
   exact reversed-(X)-arm / forward-(Y)-arm block, truncated only after
   the largest parameters needed through depth (q).  It has at most
   (2q) letters and realizes the entire suffix--prefix rectangle for that
   seam.

There are at most ((m+1)^2) seam labels in one orientation.  Hence the
total length is at most

\[
             |L_R|+O(m^2)+8q(m+1)^2.                              \tag{6.2}

The canonical line-demand degree is at most two in one orientation.  A
point belongs to one physical line of each direction, and there are four
high/low orientations.  Thus (6.2) is also a genuine bounded-copy word:
one may take a uniform multiplicity bound of (18) (two easy-system
occurrences plus at most sixteen portal-arm occurrences).  The constant is
not optimized.

Combining (5.5) and (6.2), the minimum repeat cost of the literal balanced
line-demand architecture is

\[
                         \boxed{\Theta(qm^2)}.                       \tag{6.3}
\]

Locally the minimal repair is exactly one additional copy of the inward
arm of an odd seam.  Globally, a constant-copy catalogue suffices, but an
(O(m^2))-repeat near-once braid at linear depth does not.

## 7. Consequences for the larger program

The positive complementary rectangle theorem remains intact: its swapped
baseline ((B,A)) serves the smaller doubly-missed family with only
(O(m^2)) repeats.  What fails is the proposed extension which balances
every tie-strip seam while simultaneously keeping both preferred line
systems intact.

Therefore a successful (M_m+o(m^3)) upper-band construction must relax at
least one of the following:

* use the literal balanced seam for every tie target;
* retain every preferred easy witness on an intact complete-line block;
* use only one rank-(R) spine copy.

The most plausible escape is to let mixed seams themselves replace the
easy witnesses near an inward cut, rather than demanding both the mixed
portal and the old line witness.  Incidence paths and parity cuts alone
cannot do this: the obstruction is a physical string-overlap obstruction,
not a demand-capacity obstruction.

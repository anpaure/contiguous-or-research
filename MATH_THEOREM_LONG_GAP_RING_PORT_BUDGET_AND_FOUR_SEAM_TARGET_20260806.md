# Long-gap antipodal rings reduce the global splice problem to four upper seams

## Status

Antipodal phase rings exist at every period from `2h` through `q+h-1`,
with the same fractional owner/root/upper/ticket ledger.  Choosing periods
near the upper endpoint reduces the scalar number of ring components from
`Theta(W/h)` to `Theta(W/q)`.  A loose path of prepared Boolean-C6 ports
can then merge all but at most one of those components using disjoint
collars occupying only `O(Wh/q)=O(W/sqrt q)` source positions.

The exact budget exposes one sharp constant.  The current shortest C6 port
has six unprotected immediate-upper occurrences.  The global upper surplus
can pay **exactly at most four per port** in the near-maximal schedule, and
cannot pay six for all sufficiently large parameters.  Thus the global
upper gate is no longer order-of-magnitude: it is precisely a four-seam
port, two-seam telescoping, or equivalent backup-sharing theorem.

Two natural shortcuts are impossible.  Extending period to `2h+2` and
displaying the full `h by h` common-profile tensor closes all six upper
seams, but forces two common pure-collar roots, each repeated in all three
rings: an exact four-unit root defect.  Conversely, if different ports keep
their remote labels genuinely private, all six seam masks per port are
distinct and cannot telescope.  Any four-seam construction must therefore
use a non-common tensor or deliberate cross-port sharing; extra period
alone is not enough.

This note is a scalar/topological implication.  It does not prove an
integral decomposition into long-gap rings or incidence-level assignment
of the surplus upper occurrences.

## 1. Consecutive near-maximal periods

Work on a moving ground set of size `2q-1`, and let `h` be the ambient
owner-window width.  Assume

\[
                         2h+1\le q+h-1,                 \tag{1.1}
\]

which holds at triangular depth for all sufficiently large `q`.  Put

\[
                         L=q+h-1.                        \tag{1.2}
\]

The variable-period antipodal theorem supplies phase-correct biresident
rings of both periods `L-1` and `L`, with identical symmetric fractional
ledgers.  The two periods are coprime, and their Frobenius number is

\[
                         (L-1)L-(L-1)-L=L^2-3L+1.        \tag{1.3}
\]

Since

\[
                         W_q=\binom{2q-1}{q}             \tag{1.4}
\]

is exponentially larger than (1.3), there are nonnegative integers `u,v`
such that

\[
                         W_q=u(L-1)+vL.                  \tag{1.5}
\]

Let

\[
                         c=u+v.                          \tag{1.6}
\]

Then

\[
 {W_q\over L}\le c\le {W_q\over L-1},
 \qquad
                         c=(1+o(1)){W_q\over q}.         \tag{1.7}
\]

Equation (1.5) is only the exact scalar component schedule.  Selecting
resource-disjoint rings of those lengths is the integral cover-down gate.

### Proposition 1.1 (exact maximal-period aperture)

For a fixed oriented core diamond on the `(2q-1)`-set, both periods
`L=q+h-1` and `L-1=q+h-2` are feasible.  The number of oriented anchored
lifts at either period is exactly

\[
                    (q-1)_{h-1}(q-2)!.                  \tag{1.8}
\]

#### Proof

The root contains `q-1` neutral labels and the complement of its upper
colour contains `q-2`.  The long-gap lift count at period `ell` is

\[
                 (q-1)_{h-1}(q-2)_{\ell-h-1}.
\]

For `ell=L`, the second falling factorial is `(q-2)_(q-2)=(q-2)!`;
for `ell=L-1`, it is `(q-2)_(q-3)=(q-2)!`.  At the maximal period the
common core and private set partition the entire moving ground set; at
period `L-1` exactly one neutral label is unused. \(\square\)

## 2. A bounded-degree loose connector path

Label the scheduled components `C_1,...,C_c`.  If `c` is odd, use the loose
path

\[
 \{C_1,C_2,C_3\},\{C_3,C_4,C_5\},\ldots,
 \{C_{c-2},C_{c-1},C_c\}.                              \tag{2.1}
\]

If `c` is even, use the same path through `C_(c-1)` and leave `C_c` as a
second terminal component.  The number of C6 ports is

\[
                         m=\left\lfloor{c-1\over2}\right\rfloor
                          =(1+o(1)){W_q\over2q}.          \tag{2.2}
\]

Every component participates in at most two ports.  A sealed width-`h`
C6 port uses exactly `3(2h-2)=6h-6` private collar positions, so the whole
path needs

\[
                         (6h-6)m
                         =O\left({W_qh\over q}\right)    \tag{2.3}
\]

collar incidences.  Since `h=Theta(sqrt q)`, this is

\[
                         O(W_q/\sqrt q)=o(W_q).           \tag{2.4}
\]

Locally, each long component has length `L-1` or `L` and is used by at most
two ports.  Two disjoint collars require `4h-4` positions.  Thus the
positional assertion is valid once

\[
                         q\ge3h-2,                       \tag{2.5}
\]

which holds eventually at triangular depth.  Under (2.5) there is no
scalar or positional obstruction to a collar-disjoint loose path.
Protected literal planting remains to be proved.

## 3. Exact lower and upper ledgers

The tagged C6 construction has exactly three repeated proper-source values
per port.  Hence the total local lower excess is

\[
                         3m=(3/2+o(1)){W_q\over q}.       \tag{3.1}
\]

This is `o(W_q)`.  In a `B+1` construction, the one additional position
creates a full `W_q`-scale block of short-cell capacity, so (3.1) is
scalar-negligible.  Incidence-level compiler Hall is still required.

Every owner/root factor on the child slice has one upper occurrence per
root and therefore the exact upper surplus

\[
                         E_U={2W_q\over q+1}.             \tag{3.2}

\]

The current C6 collar leaves six extreme immediate-upper occurrences
untransported per port.  If all of them need distinct backup providers,
the demand is

\[
                         6m=(3+o(1)){W_q\over q},         \tag{3.3}

\]

while (3.2) is

\[
                         E_U=(2+o(1)){W_q\over q}.        \tag{3.4}

\]

More sharply, since

\[
 m\ge {c-2\over2}\ge {W_q\over2L}-1,
\]

we have

\[
 6m\ge {3W_q\over q+h-1}-6.                             \tag{3.4a}
\]

If `q+5>2h`, the coefficient on the right of (3.4a) is strictly larger
than `2/(q+1)`.  Since `W_q` is exponential, (3.4a) exceeds (3.2) for all
sufficiently large `q`.  Thus the raw six-seam construction really exceeds
the entire unavoidable upper surplus; this is not only a leading-constant
comparison.

Conversely, any port implementation requiring at most four distinct upper
backups has total demand

\[
                         4m=(2+o(1)){W_q\over q},         \tag{3.5}

\]

and in fact lies inside the exact surplus.  Indeed,

\[
 4m<2c\le {2W_q\over L-1}
          ={2W_q\over q+h-2}
          \le {2W_q\over q+1}=E_U                       \tag{3.6}
\]

for `h>=3`.  Thus four backups per port pass the exact finite scalar test,
not merely its asymptotic version.  The same conclusion holds if
consecutive ports share or telescope two of the six seam obligations on
average.

### Proposition 3.1 (private collars forbid seam telescoping)

In the present tagged C6 port, each of its six exposed extreme uppers
contains one of the six ring-private remote labels, and those labels occur
in no other seam role.  If remote labels are also private between different
ports, then all `6m` exposed seam masks are pairwise distinct.  In
particular no two seam obligations can use the same upper occurrence
ticket, and the demand is exactly `6m`.

#### Proof

At the right extreme, after common background is suppressed, the mask in
ring `t` is

\[
                         \{a_t,a_{t+1},x_t\};            \tag{3.7}
\]

the left extreme has the analogous unique label `y_t`.  Equality of two
seam masks would force equality of their unique remote labels.  Portwise
privacy excludes this both within and between ports. \(\square\)

Hence the desired saving of two obligations per port requires a controlled
failure of remote-label privacy or a different tensor.  It cannot follow
from the current loose-path geometry alone.

## 4. The sharpened global theorem

After the long-gap and C6 results, a sufficient global construction may be
stated as follows.

1. Decompose the balanced child into phase-appropriate antipodal rings of
   periods `L-1,L` from (1.2), carrying the named lower tickets.
2. Plant the bounded-degree loose path (2.1) with serially sealed collars.
3. Transport all but at most four distinct immediate-upper obligations per
   port, or prove a two-obligation telescoping law along the path.
4. Assign the remaining backups injectively inside the exact surplus bank
   (3.2), and solve the `O(W_q/q)` lower-ticket perturbation in one terminal
   compiler.

The former `Theta(W_q/sqrt q)`-component topology problem and the apparent
`Theta(W_q/sqrt q)` upper casualty have disappeared.  What remains is a
constant-efficiency upper seam theorem plus the integral long-ring packing.

## 5. A full common-profile tensor forces four root holes

The period `2h+2` suggestion is the first case with enough physical room
for both full length-`h` collars and two opposite-arc private phases.  Its
natural marker order is

\[
 (a_{t+1},\rho_1,\ldots,\rho_{h-1},x_t,y_t,
   \lambda_{h-1},\ldots,\lambda_1,a_t).                 \tag{5.1}
\]

It does close the complete common-profile tensor through `i,j<=h`, and
therefore transports both extreme width-`h+1` uppers at every cut.  But it
is not an exact owner/root packet family.

### Theorem 5.1 (full-collar root obstruction)

Suppose three one-private-letter common-core rings expose the cyclic
three-label profiles

\[
 L_i^{(t)}=\Lambda_i\cup\{a_t\},\qquad
 R_j^{(t)}=P_j\cup\{a_{t+1}\}                           \tag{5.2}
\]

for every `1<=i,j<=h`, with cut-adjacent source letters `K+a_t` and
`K+a_(t+1)` and with active labels absent from the common profiles.
Assume all width-`h` windows are rank-`q` owners and all width-`h-1`
windows are rank-`(q-1)` roots.  Then each of the three rings contains the
same left pure-collar root `Lambda_h` and the same right pure-collar root
`P_h`.

If `Lambda_h!=P_h` and all other roots are cross-ring distinct, the three
rings have exactly four units of root repetition excess, hence exactly
four missing root colours.  If `Lambda_h=P_h`, the defect is at least five.

#### Proof

The full left cumulative union is

\[
                         L_h^{(t)}=\Lambda_h\cup\{a_t\}.
\]

It is a rank-`q` owner and `a_t` is absent from `Lambda_h`, so
`|Lambda_h|=q-1`.  Delete the cut-adjacent active source phase.  The
remaining `h-1` consecutive collar phases have union contained in
`Lambda_h`; by hypothesis that union is a rank-`(q-1)` root.  It therefore
equals `Lambda_h`, independently of `t`.  The right side is identical and
gives `P_h`.

When the two common roots are distinct, each occurs three times and hence
contributes repetition excess two, for total four.  If they coincide, one
root occurs six times and has excess five.  Root occurrences and required
root colours have equal cardinality, so repetition excess equals the
number of missing roots. \(\square\)

For (5.1), the two repeated roots are explicitly

\[
 K\cup\{\rho_1,\ldots,\rho_{h-1}\},\qquad
 K\cup\{\lambda_1,\ldots,\lambda_{h-1}\}.              \tag{5.3}
\]

The opposite-arc private phases `x_t,y_t` do not meet either interval and
cannot distinguish them.  Therefore increasing the period to `2h+2`
trades six upper seam obligations for four exact lower-root holes; it does
not close the coloured factor.

Theorem 5.1 applies to the common-profile tensor (5.2), not to every
conceivable three-way boundary tensor.  A successful four-seam theorem
must use ring-dependent profiles whose union multisets still satisfy the
general three-cut criterion, or deliberately coalesce and repair the four
root units.  Neither construction is supplied here.

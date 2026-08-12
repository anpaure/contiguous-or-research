# A Johnson-square collar turns the ternary hex into a planted cycle actuator

Date: 2026-08-01  
Status: exact constant-size cycle actuator and bounded-bank Delcourt--Postle
extension.  The old state has one directed four-cycle and two isolated
edges; the new state has two directed paths, with exactly the same lower,
upper, tail and head resources.

## 1. Construction

Fix an oriented target atom

\[
 e=(L,U,E,F),\qquad E=L+d,\quad F=L+a,\quad U=L+a+d.     \tag{1.1}
\]

Choose

\[
 b,x\in L,\quad b\ne x,
 \qquad
 c,y\notin U,\quad c\ne y.                              \tag{1.2}
\]

Use `(b,c)` for the ternary-hex packet.  Its old and new phases are

\[
 O=\{AB,CD,EF\},\qquad N=\{AF,CB,ED\},                  \tag{1.3}
\]

with

\[
\begin{array}{ll}
 A=U-b,&B=L-b+a+c,\\
 C=L-b+c+d,&D=L+c.
\end{array}                                               \tag{1.4}
\]

Now put

\[
                         X=L-x+a+y,\qquad Y=L-x+d+y.       \tag{1.5}
\]

The three directed Johnson edges

\[
                         R=\{FX,XY,YE\}                   \tag{1.6}
\]

have typed outer resources

\[
\begin{array}{c|c|c}
 &\text{lower}&\text{upper}\\ \hline
 FX&L-x+a&L+a+y\\
 XY&L-x+y&L-x+a+d+y\\
 YE&L-x+d&L+d+y.
\end{array}                                               \tag{1.7}
\]

Define the two six-atom gadget states

\[
                         G^-=O\cup R,
             \qquad      G^+=N\cup R.                    \tag{1.8}
\]

### Theorem 1.1 (exact cycle actuator)

Both `G^-` and `G^+` are four-resource matchings, and

\[
                         res(G^-)=res(G^+)                \tag{1.9}
\]

in every typed resource class.

The physical graph of `G^-` is the disjoint union of

* the directed four-cycle

  \[
                         E-F-X-Y-E,                        \tag{1.10}
  \]

* the isolated directed edge `AB`; and
* the isolated directed edge `CD`.

The physical graph of `G^+` is the disjoint union of the two directed paths

\[
                         A-F-X-Y-E-D,
             \qquad      C-B.                             \tag{1.11}
\]

Thus the toggle `G^- -> G^+` removes exactly one physical cycle, creates no
palette defect, and returns two path components.

#### Proof

The ternary-hex identity gives `res(O)=res(N)`.  The three collar atoms `R`
are unchanged, so (1.9) follows once both states are matchings.

Formula (1.7) is obtained by taking the intersections and unions of the
successive vertices in (1.5).  The conditions `b!=x` and `c!=y`, together
with the four membership patterns in the distinguished coordinates `a,d`,
show that the collar's three lower and upper colours are distinct from one
another and from the packet colours.  The eight physical vertices

\[
                         A,B,C,D,E,F,X,Y                  \tag{1.12}
\]

are distinct.  In `G^-`, every one occurs once as a tail and once as a head
only where shown in (1.10), while `AB,CD` use the remaining private roles.
The same direct check applies to `G^+`.  Hence both states are typed
four-resource matchings.

The old physical decomposition is immediate from `EF union R`.  Replacing
`AB,CD,EF` by `AF,CB,ED` turns the broken cycle path

\[
                             F-X-Y-E
\]

and the four endpoints of the two deleted isolated edges into exactly the
two paths (1.11).  `square`

For one target there are exactly

\[
                       [(m-1)(m-2)]^2                  \tag{1.13}
\]

indexed collars of this form.

## 2. Bounded actuator banks

### Lemma 2.1 (fixed forbidden bank removes only `O(m^3)` collars)

Fix one target `e` and one typed outer resource or physical middle vertex
not forced by `e`.  Among the parameter quadruples `(b,x,c,y)` in (1.2), at
most `O(m^3)` produce a gadget using that fixed unit outside the target
roles.  The constant is absolute and uniform in the fixed unit.

#### Proof

Every non-target resource or physical vertex in (1.4)--(1.7) is obtained
from `L` by deleting at most one of `b,x` and adjoining a specified subset
of `a,d,c,y`.  Equality with a fixed set determines at least one of the four
parameters; the other three then have at most `m` choices each.  There are
only a fixed number of displayed formulas.  The union bound is `O(m^3)`.
`square`

### Corollary 2.2 (every fixed target bank has private cycle actuators)

Let `e_1,...,e_H` be pairwise typed-resource-disjoint target atoms, with
pairwise disjoint **physical endpoint sets**, and with `H` fixed.  For all
sufficiently large `m`, choose one collar per target so that

* all non-target typed outer resources are distinct;
* all non-target physical vertices are distinct and avoid every target
  endpoint.

Then the unions

\[
                         B^- =\bigcup_i G_i^- ,
              \qquad     B^+ =\bigcup_i G_i^+             \tag{2.1}
\]

are four-resource matchings.  The old bank has exactly `H` directed
four-cycles and `2H` isolated edge components; the new bank is a physical
linear forest.  The two banks have exactly the same complete typed support.

#### Proof

Each menu has `Theta(m^4)` choices by (1.13).  At a greedy step there are
only `O(H)` fixed forbidden units, and Lemma 2.1 removes `O_H(m^3)` choices.
For fixed `H` a choice remains.  The component statements follow packet by
packet.  The assumed physical disjointness of the target edges then makes
the component decomposition a disjoint union of the one-gadget
decompositions.  `square`

## 3. Rebuild a Delcourt--Postle body around either phase

For every gadget reserve

* its six lower and six upper colours; and
* both tail/head copies of its eight physical vertices.

The resulting closed support has size at most

\[
                              28H.                       \tag{3.1}
\]

Delete it from the ordered-diamond host and apply the valid fixed-girth
Delcourt--Postle colouring theorem.  Exactly as in the planted fixed-bank
theorem, for fixed `g` one obtains a physically disjoint forest `F` with

\[
 |F|\ge N-ND^{-\alpha_g}-{N\over g+1}-28H.             \tag{3.2}
\]

Therefore

\[
                       F\cup B^- \longrightarrow F\cup B^+   \tag{3.3}
\]

is a simultaneous palette-neutral conversion from a near-perfect body with
exactly `H` planted physical cycles to a near-perfect physical linear
forest.

This is the positive joint counterpart to the hex-free obstruction: cycle
actuators may be installed before the bulk is chosen, but cannot be
extracted from an arbitrary bulk afterward.

## 4. Scope for `B(k)+O(1)`

For bounded regenerative defect, the central cycle sidecar is now explicit:
one eight-vertex/six-atom actuator per named cycle state, with no loss of any
of the four immediate palettes.  What remains is to prove that the
same-parity lift exports its bounded cycle debt in these named square-collar
states, rather than as arbitrary cycles.  The one-cell star-hidden
fan/crossing identity and the common-cap tickets still have to be carried on
the collar; they are not consequences of the central resource identity.

## 5. Replay

Run

```text
python3 scratch/audit_boolean_hex_square_collar_cycle_actuator_20260801.py
```

The replay checks every parameter quadruple for one canonical target at
`3<=m<=7`, all typed resource identities, the exact old/new component
shapes, and the count (1.13).

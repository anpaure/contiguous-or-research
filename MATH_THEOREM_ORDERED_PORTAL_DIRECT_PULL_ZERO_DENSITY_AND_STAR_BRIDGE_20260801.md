# Ordered portals versus canonical pulls: exact parenthesis criterion, zero direct density, and the star bridge

Date: 2026-08-01

Status: unconditional for the standard plane-tree gluing multigraph and its
Dyck/parenthesis coordinates.  Transfer from an abstract plane-tree label to
a literal GMN lexical-factor occurrence still requires the existing
occurrence-provenance predicate.  This note rules out a linear **direct**
ordered-portal menu inside the canonical pull labels; it does not rule out
occurrence-labelled packet expansions on one or both decorated rails.

## 0. Outcome

Two exact obstructions close the naive portal-to-canonical-pull lift.

1. A canonical pull pair differs by one cyclically adjacent parenthesis
   interchange `110 <-> 101`.  Therefore a portal star

   \[
      p\longrightarrow p-z+\beta
   \]

   with fixed `p,z` contains at most two direct canonical pulls, and at most
   one in a fixed orientation.  The robust ordered-shift list has
   `Theta(m)` heads.  Its direct-pull density is consequently `O(1/m)`, not
   positive density.  In the native linear order, the only possible member
   of the certified list is the cyclic wrap neighbour.
2. The labelled plane-tree pull multigraph has edge-connectivity exactly

   \[
                              \lambda(H_n)=1
                                                        \tag{0.1}
   \]

   for every `n>=3`.  The star plane tree is incident with one allowed pull
   label.  Thus no cardinality estimate of the form
   `|B_D|=O(d)=o(n)` can imply that a transparency-filtered pull host remains
   connected.  The unique star bridge has to be protected explicitly.

The abstract rail picture is the opposite: every Johnson edge lies in
`n(n-1)` incidence-hex rail frames.  However, inside one fixed canonical
factor the complete decorated pull family gives at most eight rail heads at
one fixed tail.  Hence the shortage is not set-theoretic hex supply.  It is
the canonical parenthesis occurrence, external-stub, and transparent-host
requirement.

## 1. Standard pull coordinates

Use the Dyck convention in which `1` opens and `0` closes.  Let `D_n` be the
Dyck words of length `2n`.  Root rotation identifies the words encoding the
same plane tree.

The standard Mütze/Merino--Mička gluing labels are

\[
                    x=110u0v,
       \qquad       y=101u0v,                         \tag{1.1}
\]

with `u,v` Dyck.  Labels whose two words encode the same plane tree are
loops and are omitted, as is the standard exceptional star label.  The
auxiliary multigraph `H_n` has plane-tree classes as vertices and one
labelled edge `[x][y]` for each remaining pair (1.1).

For a physical lower middle-level word of length `2n+1`, the canonical
cycle-lemma rotation has the form `x0` with `x in D_n`.  Thus two literal
lower words `p,q` carry one direct gluing label precisely when one common
cyclic shift gives

\[
               \sigma^j(p)=110u0v0,
       \qquad  \sigma^j(q)=101u0v0,                  \tag{1.2}
\]

or the reverse, with the nonloop/exceptional exclusions above.

The equivalent nested GMN parenthesis normal form is

\[
\begin{aligned}
x={}&1u_1,1u_2\cdots1u_t\,110w0\,
                       v_t0\cdots v_10v_0,\\
y={}&1u_1,1u_2\cdots1u_t\,101w0\,
                       v_t0\cdots v_10v_0,
\end{aligned}                                        \tag{1.3}
\]

up to its declared cyclic phase, with every displayed subword Dyck.  At the
plane-tree level, (1.3) says exactly that a pending rightmost leaf edge is
pulled from a vertex to its predecessor (or the inverse operation).

For the later rotational factor, (1.1)--(1.2) are a literal occurrence
criterion.  For the canonical lexical GMN factor, (1.3) is the canonical
pull criterion, while identification with a specified rotational occurrence
also requires the already-defined predicate `Prov`: the six ports, three old
factor incidences, and six untouched external stubs must agree.  Equality of
the two changed owner masks alone is not that provenance statement.

## 2. Direct ordered-shift intersection

### Theorem 2.1 (two-neighbour bound)

Fix a literal rank-`n` word `p` and one present coordinate `z`.  Among all
Johnson neighbours

\[
                  q_\beta=p-\{z\}+\{\beta\},
                  \qquad \beta\notin p,              \tag{2.1}
\]

at most two can be direct canonical pull pairs with `p`.  With one fixed
pull orientation, at most one can occur.

#### Proof

Equations (1.2)--(1.3) show that the two changed coordinates are the two
positions in the local interchange

\[
                            110\leftrightarrow101.     \tag{2.2}
\]

They are adjacent in the cyclic coordinate order.  A fixed coordinate `z`
has only two cyclic neighbours.  Once the direction `110 -> 101` is fixed,
only the forward neighbour has the required deleted/inserted roles. \(\square\)

### Corollary 2.2 (zero density in the robust portal list)

At an ordered-flag root

\[
                     z_1\prec z_2\prec\cdots\prec z_n,
\]

the certified portal list is

\[
 \mathcal L(p)=
 \{p-z_1+\beta:\ z_d\prec\beta,\ \beta\notin p\}.   \tag{2.3}
\]

Consequently

\[
 |\mathcal L(p)\cap E(H_n)|\le2,
 \qquad
 { |\mathcal L(p)\cap E(H_n)|\over|\mathcal L(p)| }
      =O(1/n)                                         \tag{2.4}
\]

whenever the robust list has linear size.

If `prec` is the linearization of the same cyclic coordinate order used in
the parenthesis model, then the nonwrap neighbour of `z_1` lies strictly
before `z_2`, hence before `z_d` for `d>=2`.  The predecessor of `z_1` lies
before it unless `z_1` is the first coordinate.  Therefore

\[
        |\mathcal L(p)\cap E(H_n)|\le1,               \tag{2.5}
\]

and the sole possible case is the cyclic wrap from the first coordinate to
the last.  The full Dyck factorization (1.2), not adjacency alone, still has
to hold, so even that candidate may be absent.

This is a sharp zero-density obstruction to identifying the ordered-shift
heads themselves with canonical auxiliary pull labels.  It is independent
of residence, compiler, and upper-colour constraints.

## 3. Pivot geodesics

The sharp pivot geodesic has transitions

\[
 M_{j+1}=M_j-\{\lambda_{j+1}\}+\{\rho_{j+1}\}.
                                                        \tag{3.1}
\]

### Corollary 3.1 (direct-pull pivot criterion)

Transition `j` is a direct canonical pull if and only if

1. `lambda_(j+1)` and `rho_(j+1)` are cyclic neighbours; and
2. after the common cycle-lemma rotation, the complete surrounding word has
   the Dyck factorization (1.2), equivalently the pending-leaf condition in
   (1.3).

Thus a set-theoretic pivot geodesic, even one with perfect Johnson and q1
palettes, is not automatically a path in the canonical pull host.  A
relabelling can deliberately make its disjoint active pairs adjacent, but
that is a new correlated parenthesis construction and does not follow from
the aperture theorem.

## 4. Every Johnson edge is an abstract rail edge

The preceding obstruction concerns **direct auxiliary labels**, not
decorated incidence rails.

Let `p=I+e` and `q=I+b` be any Johnson edge on rank `n`, so `|I|=n-1`.
Choose

\[
                  a\in I,
       \qquad     c\notin I\cup\{b,e\},
       \qquad     H=(I-\{a\})\cup\{e\}.             \tag{4.1}
\]

Then

\[
                 p=H+a,
       \qquad    q=H-e+a+b,                          \tag{4.2}
\]

which is one edge of the common-delete decorated rail of the incidence
hexagon with core `H`, active labels `a,b,c`, and external deleted label
`e`.

On a `2n+1`-element ground set there are exactly

\[
                         (n-1)n                       \tag{4.3}
\]

choices in (4.1): `n-1` choices for `a` and `n` choices for `c` outside the
`n+1` element union `p union q`.

### Theorem 4.1 (abstract rail abundance)

Every rank-`n` Johnson edge lies in `n(n-1)` labelled abstract incidence
pull rails.

This does not contradict Corollary 2.2.  To turn one frame into a canonical
physical pull one must also realize:

* the parenthesis pair (1.3);
* the literal three old factor incidences;
* all six untouched external stubs;
* the required second decorated rail when the packet changes both shores;
* the retained fragments, boundary marks, and clipped ages; and
* membership of the corresponding auxiliary label in a transparent
  spanning host.

The existing occurrence-expansion criterion is exactly this missing list.
For example, in the rotational standard model a full two-rail coatom packet
requires the `u=empty` coherent subfamily, which is already known to be
disconnected for `n>=5`.

### Theorem 4.2 (constant canonical decorated-rail degree)

Let `F` be the canonical two-factor and let `Z` range over its pairwise
edge-disjoint alternating pull hexagons.  Form the complete decorated turn
rails by adjoining, at every hexagon port, the unchanged external factor
stub.  At every fixed rank-`n` owner `p`, the union of all rank-`n` rail
edges has degree at most eight.  Consequently any ordered-shift list at `p`
contains at most eight heads which occur even as a decorated rail edge of a
canonical pull.

#### Proof

The factor gives `p` two incident factor edges.  A pull in which `p` is a
hexagon port uses one of those two edges as its old alternating edge.  Since
the pull hexagons are edge-disjoint, at most two pulls use `p` as a port.

A rail can also contain `p` as the unchanged external endpoint at a
neighbouring opposite-shore vertex `U`.  Fix the factor edge `pU`.  Such a
pull must use the **other** factor edge at `U` as its old hexagon edge.
Again edge-disjointness permits at most one such pull for each of the two
choices of `U`.  Hence at most two further pulls use `p` as an external rail
endpoint.

One incidence hexagon gives degree at most two at `p` in the decorated
Johnson rail: one old and one new turn through its relevant port(s).  Thus

\[
                         \deg_{\rm rail}(p)
                         \le(2+2)\cdot2=8.            \tag{4.4}
\]

Restricting to the certified ordered-shift heads can only decrease this
number. \(\square\)

The constant eight is deliberately a safe universal bound; overlaps can
make the true degree smaller.  Unlike Theorem 2.1, it does not identify the
portal itself with the plane-tree auxiliary edge.  It therefore closes both
readings of the naive linear-menu claim:

\[
 \begin{array}{c|c}
 \text{direct auxiliary pull labels at fixed tail/deletion}&\le2,\\
 \text{all canonical decorated-rail heads at fixed tail}&\le8.
 \end{array}                                         \tag{4.5}
\]

Neither family has positive density in a robust list of order `n`.

## 5. Exact edge-connectivity of the pull host

Let

\[
                         S_n=[(10)^n]                 \tag{5.1}
\]

be the star plane-tree class.

### Theorem 5.1 (unique star bridge)

For every `n>=3`, the star vertex `S_n` has degree one in the labelled
standard pull multigraph.  Its unique incident allowed label is

\[
       x_\star=1100(10)^{n-2},
       \qquad
       y_\star=1010(10)^{n-2}=(10)^n.                \tag{5.2}
\]

Consequently

\[
                         \boxed{\lambda(H_n)=1}.       \tag{5.3}
\]

#### Proof

A star has only two rooted ordered-tree words: rooting at the centre gives
`(10)^n`, and rooting at a leaf gives

\[
                         1(10)^{n-1}0.                \tag{5.4}
\]

For the star to be the target `y=101u0v` of a gluing pair, (5.1) forces

\[
                         u=\varnothing,
       \qquad           v=(10)^{n-2},                \tag{5.5}
\]

and hence forces the unique source in (5.2).

For the star to be the source `x=110u0v`, the only possibility is the
leaf-rooted word (5.4).  Its gluing pair is precisely the standard
exceptional star label, which is excluded from the auxiliary host.  Thus
(5.2) is the only allowed incident label.

The plane-tree pull graph is connected by the canonical gluing theorem, so
its edge-connectivity is at least one.  The singleton cut `{S_n}` has size
one, proving (5.3). \(\square\)

The bridge (5.2) has `u=empty` in (1.1).  Hence it survives the rotational
all-six-coherent filter used by the full coatom packet.  The proved
disconnection of that filtered family is therefore caused by additional
cuts deeper in the plane-tree graph; merely reserving the star bridge does
not cure that filtered-host obstruction.

### Corollary 5.2 (transparency cardinality cannot work)

Let `B_D` be the set of pull labels forbidden by a protected packet bank.
The generic sufficient inequality

\[
                            |B_D|<\lambda(H_n)         \tag{5.6}
\]

reduces here to `B_D=emptyset`.  In particular, an estimate
`|B_D|=O(d)=o(n)` gives no connectivity guarantee.

At the factor-edge level, canonical pull hexagons are pairwise
edge-disjoint.  Therefore, if `D_E` is a set of protected factor incidences,
then

\[
                       |B_D^{\rm edge}|\le |D_E|.      \tag{5.7}
\]

This is the best automatic cardinality statement.  Full packet interfaces
also protect vertices, turns, interval witnesses, and boundary signatures.
There is a second local bound.  Every pull touching a physical factor vertex
uses one of the two base-factor edges at that vertex.  Pull hexagons are
edge-disjoint, so at most two pull labels touch one vertex.  Hence, for a
protected vertex halo `D_V`,

\[
                    |B_D^{\rm vertex}|\le2|D_V|.       \tag{5.8}
\]

A fixed packet bank therefore forbids only `O(hd)` pulls by literal
edge/vertex overlap.  If the protected interface includes all decorated
turns through neighbouring opposite-shore vertices, the proof of Theorem
4.2 gives the safe load four rather than two per protected vertex; this is
still `O(hd)`.  These bounds remain useless as a *uniform connectivity*
estimate because `lambda(H_n)=1`.  Moreover, (5.7)--(5.8) do not bound pulls
forbidden by nonlocal chronology, nesting, interval-witness, or common-cap
conditions; those can declare a disjoint pull nontransparent.

Every transparent completion must, at minimum, certify that the unique star
bridge (5.2) remains allowed or prescribe it in advance.  Even after doing
so, the host has another constant cut.

Let

\[
                    P_n=[10\,1^{n-1}0^{n-1}]          \tag{5.9}
\]

be the plane path class.  Inspecting the possible first rooted branch shows
that exactly two gluing labels meet `P_n`:

\[
\begin{aligned}
 110\,1^{n-2}0^{n-1}
   &\longleftrightarrow 101\,1^{n-2}0^{n-1},\\
 1100\,1^{n-2}0^{n-2}
   &\longleftrightarrow 1010\,1^{n-2}0^{n-2}.
\end{aligned}                                        \tag{5.10}
\]

Both other endpoints encode the same neighbouring plane tree.  For
`n>=4`, `P_n` is distinct from the two endpoints of the star bridge.
Therefore contraction of the star bridge leaves a two-edge singleton cut:

\[
                   \lambda(H_n/e_\star)\le2.          \tag{5.11}
\]

Indeed, a rooted path with ordered branch lengths `a,n-a` begins `110`
only for `a=2`, giving the second label in (5.10); it begins `101` only
when its first branch has length one, giving the first.  This proves that
the list is complete.

The finite O3 audit below finds equality in (5.11) for `4<=n<=10`.  Only
the upper bound is used here.  Thus even reserving the unique bridge does
not produce growing cut robustness.

## 6. Consequence for the forest-first route

The forest-first graphic extension theorem remains correct, but its physical
hypothesis must now be read literally.

* A robust ordered-shift menu does **not** give a linear menu of canonical
  pull labels; direct intersection is at most two, and even the complete
  decorated-rail intersection is at most eight.
* Abstract incidence-rail realizations are quadratic, but they do not carry
  canonical occurrence provenance.
* The canonical host is not robust under deletion by cardinality; its
  minimum cut is one.

Therefore the remaining positive statement cannot be a degree/expansion
argument inside the unmodified canonical host.  It must do at least one of:

1. plant the bounded task packets directly on specially chosen canonical
   pull occurrences while explicitly reserving the star bridge and every
   other required transparent cut;
2. use a noncanonical base factor with a new compatible connector family;
3. enlarge a pull to a longer occurrence-labelled packet whose auxiliary
   host has genuinely redundant cuts; or
4. construct the final upper-decorated Hamilton path prospectively, so no
   fixed canonical pull host is filtered afterward.

This is a sharp negative answer to the naive portal-to-static-pull lift, not
to the broader prospective Catalan/pivot programme.

There is also an independent global reason not to promote this canonical
host to the entire carrier construction: the lexical base plus any canonical
pull spanning tree retains a positive projected upper-colour defect for
`m>=12`.  The present note is stronger only on the topology/interface row.
A useful all-dimensional construction must therefore use a nonlexical host,
noncanonical long switches, or separately charged cross-boundary upper
witnesses even if the bounded portal occurrences themselves are calibrated
against canonical pulls.

## 7. O3 replay

The independent source

```text
scratch/audit_gmn_pull_direct_portal_and_edge_connectivity_20260801.cpp
```

enumerates Dyck words, rooted plane-tree classes, every standard gluing
label, and the labelled global minimum cut by Stoer--Wagner.  It also checks
that one rooted tail/deleted-coordinate pair has at most one oriented direct
gluing head.

The run was compiled with `g++ -O3` and executed on the H100 host CPU, not
on the local machine.  For `3<=n<=10` it gives

```text
edge_connectivity = 1
max_direct_rooted_tail_delete = 1
```

in every dimension.  It identifies `(10)^n` as the unique degree-one star
class for `n>=4`, with the bridge (5.2), and reports equality in the
contracted-star upper bound (5.11) through `n=10`.

Frozen output:

```text
scratch/audit_gmn_pull_direct_portal_and_edge_connectivity_20260801.txt
```

Source SHA-256 begins `cdff3ae617742261`; output SHA-256 begins
`11103faa958dcf25`.  The enumeration is supporting replay; Theorems 2.1 and
5.1 are the symbolic proofs.

# A coatom-link cycle has one forced short run, and one cut makes all of its runs boundary-clipped

Date: 2026-08-01  
Lane: Thread D, planted-host residence interface  
Status: exact abstract theorem, with the missing cyclic-simplicity and
boundary-gluing hypotheses made explicit.

## 0. Verdict

The informal claim is correct for a **simple cyclic coatom link**, but false
under the weaker statement “`d+1` owners and `d` Johnson transitions in a
`d`-element link.”

Let `d>=3`, let `X` and `D={x_0,...,x_(d-1)}` be disjoint, and assume

\[
 |X|=r-d+1,
 \qquad R_i=D\setminus\{x_i\},
 \qquad T_i=X\cup R_i.                                  \tag{0.1}
\]

Choose any cyclic ordering of the `x_i`, and write the closed owner walk as

\[
                  T_0,T_1,\ldots,T_{d-1},T_d=T_0.       \tag{0.2}
\]

Every owner has rank `r`, and all `d` transitions are Johnson.  In the
repeated-end linearization (0.2), coordinate `x_0` has trace

\[
                         0\,1^{d-1}\,0.                 \tag{0.3}
\]

Thus a residence rule forbidding internal positive runs shorter than
`d+1` (indeed, shorter than any threshold at least `d`) rejects (0.2).
Intrinsically, on the cyclic `d`-owner chronology every link coordinate has
one cyclic positive run of length `d-1`.  The repeated-end display merely
makes the run belonging to the cut label `x_0` visibly internal; the other
`d-1` cyclic runs wrap through the displayed boundary.

Cut the closing edge and keep only

\[
                         T_0,T_1,\ldots,T_{d-1}.         \tag{0.4}
\]

Then every positive run of every coordinate in `X union D` meets a boundary
of this path component.  A link coordinate omitted at an interior owner has
two clipped boundary runs; the coordinate omitted at an endpoint has one.
Every coordinate of `X` has the single clipped trace `1^d`.  Hence (0.4)
has no short **internal** run.

This is a componentwise statement.  If both path ends are subsequently
glued into an ambient chronology, clipping disappears.  Each endpoint run
must then be extended to the residence threshold, or one endpoint must
remain a genuine global boundary.  The cut alone is not an ambient
residence theorem.

The exact palette ledger is:

* `d` distinct rank-`r` owners;
* `d` distinct cyclic lower colours

  \[
     C_i=T_i\cap T_{i+1}
       =X\cup\bigl(D\setminus\{x_i,x_{i+1}\}\bigr),     \tag{0.5}
  \]

  for `d>=3`;
* one upper colour

  \[
                       U=T_i\cup T_{i+1}=X\cup D,        \tag{0.6}
  \]

  of multiplicity `d`.

After opening, `d-1` lower colours remain internal and the cut colour
`C_(d-1)` is one exact boundary/compiler obligation.  The upper support is
unchanged as a set (provided `d>=3`), because every remaining transition
still has union `U`.

## 1. Minimal cyclic-link theorem

### Theorem 1.1

Let `T_0,...,T_d` satisfy (0.1)--(0.2).  Then:

1. `T_0,...,T_(d-1)` are distinct rank-`r` owners;
2. every `T_i T_(i+1)` is a Johnson edge;
3. the lower colours (0.5) are distinct;
4. all upper colours equal (0.6);
5. the repeated-end word has the internal run (0.3); and
6. after deleting `T_d`, every positive coordinate run touches at least one
   component boundary.

#### Proof

The sets `R_i` are the `d` coatoms of `D`, so they and hence the owners are
distinct.  Consecutive owners exchange `x_i` and `x_(i+1)`, proving the
Johnson row.  Their intersection and union are exactly (0.5)--(0.6).

The unordered omitted pairs `{x_i,x_(i+1)}` are the edges of a simple
`d`-cycle, and are distinct for `d>=3`; hence so are the lower colours.

Coordinate `x_0` is absent precisely at `T_0=T_d`, proving (0.3).  In the
opened word (0.4), a link coordinate `x_j` is absent at exactly one
position.  If that position is internal, the positive trace is a prefix
and a suffix; if it is an endpoint, it is one boundary run.  Coordinates
of `X` are present everywhere, giving `1^d`.  This proves the residence
statement.  \(\square\)

### Corollary 1.2 (exact seam debt)

Opening the cycle removes exactly one physical owner edge and exactly one
lower-colour occurrence.  Because the cyclic lower colours are distinct,
that colour has no other occurrence inside this link packet.  An exact
lower-rainbow construction must therefore assign it injectively to a seam,
boundary cell, or external compiler cell.

No analogous distinct upper debt is created: the upper target `U` remains
represented by each of the `d-1` internal edges.

## 2. Why the weaker formulation is false

Assume only that each `R_i` is a `(d-1)`-subset of one `d`-set and that
consecutive owners are Johnson.  The link graph is `J(d,d-1)=K_d`; this
condition allows arbitrary walks in `K_d`.

For example, with `d=4`, alternate two coatoms:

\[
 R_0,R_1,R_0,R_1,R_0.                                  \tag{2.1}
\]

It has four Johnson transitions, but does not visit the four coatoms, its
owner and lower palettes repeat, and its coordinate traces are not those of
Theorem 1.1.  More generally, even requiring the first `d` states distinct
does not force `R_d=R_0`; the last edge may close a shorter cycle and leave
a tail.

Therefore the minimum sufficient hypothesis is not a scalar transition
count.  It is:

\[
 \boxed{
  \text{the distinct owner support is all }d\text{ coatoms, and the }d
  \text{ edges form their simple cycle}.}               \tag{2.2}
\]

Equivalently, after cyclic indexing, every link label is omitted once and
`R_d=R_0`.

## 3. Exact boundary-residence condition after gluing

Let the opened packet (0.4) be inserted between exterior owner words `L`
and `R`.  Componentwise clipping proves ambient residence only under an
additional collar condition.

For each coordinate `y` present at the left endpoint, let `lambda_L(y)` be
the consecutive number of `y`-owners immediately preceding the packet; set
it to infinity when the left endpoint is a global boundary.  Define
`lambda_R(y)` analogously.  Every positive packet segment touching only the
left boundary must satisfy

\[
        \lambda_L(y)+\text{(its packet-prefix length)}\ge h, \tag{3.1}
\]

and analogously on the right, where `h` is the required run floor.  If a
coordinate has positive packet pieces on both sides of its unique zero,
the two inequalities are separate; the zero prevents them from joining.
For `y in X`, the packet is all ones, so if both exterior neighbours also
contain `y`, the two collars and packet form one run; otherwise the
corresponding finite side must make its resulting run at least `h`.
More explicitly, when neither side is a global boundary its required run
length is

\[
 d+\mathbf 1_{\{y\text{ continues left}\}}\lambda_L(y)
   +\mathbf 1_{\{y\text{ continues right}\}}\lambda_R(y), \tag{3.2}
\]

and this must be at least `h`; a global boundary clips that end instead.

These inequalities are necessary and sufficient because the packet trace
of every coordinate has at most one zero.  They are the exact socket row
missing from the bare cut statement.

At the target depth of the octagon application, take `h=d+1`.  Then no
finite packet piece of length at most `d` is independently safe; it must be
clipped or extended by a collar.

## 4. Common-cap and owner assumptions

All owners lie in the rank-`r+1` set

\[
                             Q=X\cup D.                 \tag{4.1}
\]

Thus `Q` is a common set-theoretic cap.  This does not by itself give a
rank-`r` compiler cap or a common antecedent source word.  A physical use
still needs:

1. one literal source/deadline realization of the owners (0.4);
2. the collar inequalities (3.1);
3. an injective host for the missing lower colour of Corollary 1.2; and
4. all other protected target/common-cap matching rows.

The theorem concerns owner traces.  It neither supplies nor assumes the
seven planted source hosts of the octagon menu.

## 5. Replay

Run

```text
python3 scratch/audit_threadD_link_cycle_residence_cut_20260801.py --write
```

The dependency-free replay checks `3<=d<=64`, arbitrary deterministic
cyclic orders, owner ranks, Johnson steps, lower/upper palette counts, the
forced `0 1^(d-1) 0` trace, and the complete clipped-run classification
after opening.

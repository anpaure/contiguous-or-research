# Every internal octagon ray anchor creates a rank-deficient owner valley when split

Date: 2026-08-01  
Lane: AD, physicalization of the sharp octagon `8/9` native-ray bank  
Status: exact all-`d` flat-host obstruction and corrected anchor census for
`d>=5`.  The result does not exclude planted exterior hosts, coordinated
multi-position rethreads, or genuinely nonflat variable-deadline compilers.

## 0. Verdict

The frozen `8/9` native endpoint-ray partitions contain **seven internal
anchors in each phase**, not seven in phase zero and eight in phase one.  In
phase one the anchor

\[
                            R(9d+25)
\]

is the packet-near half of the exterior right host.  The expanded sharp
source has two left-host positions, then the sharp source, then two
right-host positions, so an internal expanded coordinate `e` maps to the
sharp coordinate `p=e-2`.

None of the fourteen internal anchors can be made a legal single binary
split host for a flat depth-`d`, rank-`r` owner chronology.  This failure is
independent of the decomposition

\[
                         Q_p=Z\cup T,
                 \qquad Z,T\ne\varnothing.              \tag{0.1}
\]

Indeed, every such split forces `d` new owner windows which do not contain
an endpoint fragment at all.  Each is contained in the intersection of two
adjacent old rank-`r` Johnson owners and hence has rank at most `r-1`.
Consequently owner rank fails before deadline, residence or common-cap
choices can help.

This is a flat physical-host obstruction, not an OR-deck obstruction.
Full-block lifting still preserves every old interval OR, but every old
length-`d+1` owner occurrence crossing the split becomes length `d+2`.
Using that lift therefore requires a one-position deadline relaxation or a
different occurrence.  A nonflat generalized compiler may exploit such a
relaxation; the present theorem does not rule it out.

## 1. Universal split-window identity

Let

\[
 Q=(Q_0,\ldots,Q_{N-1}),\qquad
 O_i=\bigcup_{q=i}^{i+d}Q_q\quad(0\le i<L)              \tag{1.1}
\]

be a source for a rank-`r` Johnson path
`O_0,...,O_(L-1)`, with `N=L+d`.  Fix

\[
                         d\le p\le L-1                  \tag{1.2}
\]

and replace `Q_p` by the ordered pair `Z,T` in (0.1).  Write
`Q tilde` for the expanded source and

\[
                 \widetilde O_i=\bigcup_{q=i}^{i+d}\widetilde Q_q
                  \qquad(0\le i\le L).                 \tag{1.3}
\]

### Theorem 1.1 (exact new depth-`d` owner windows)

The new windows are

\[
\widetilde O_i=
\begin{cases}
O_i,&i\le p-d-1,\\
\displaystyle\bigcup_{q=p-d}^{p-1}Q_q\cup Z,&i=p-d,\\
C_s,&i=p-d+s,\quad1\le s\le d,\\
\displaystyle T\cup\bigcup_{q=p+1}^{p+d}Q_q,&i=p+1,\\
O_{i-1},&i\ge p+2,
\end{cases}                                             \tag{1.4}
\]

where

\[
                 C_s=\bigcup_{q=p-d+s}^{p+s-1}Q_q.      \tag{1.5}
\]

In particular all `C_s` are independent of `Z,T`.

#### Proof

Before the split the indices agree; after both pieces they are shifted by
one.  The first crossing window ends at `Z`, the last begins at `T`, and a
strictly intermediate window contains both `Z,T` but has only `d-1` other
pieces.  Replacing `Z union T` by `Q_p` gives exactly (1.4)--(1.5).  \(\square\)

### Theorem 1.2 (universal flat-rank obstruction)

For `1<=s<=d`, put `a=p-d+s`.  Then

\[
 C_s\subseteq O_{a-1}\cap O_a.                          \tag{1.6}
\]

Since consecutive owners are distinct adjacent rank-`r` Johnson vertices,

\[
                       |O_{a-1}\cap O_a|=r-1.           \tag{1.7}
\]

Therefore

\[
                         |C_s|\le r-1                   \tag{1.8}
\]

for all `s`.  No choice of nonempty `Z,T` with union `Q_p` makes the expanded
depth-`d` dilation a rank-`r` word.

#### Proof

Every index in `[a,a+d-1]` belongs to both source windows
`[a-1,a+d-1]` and `[a,a+d]`, giving (1.6).  Equation (1.7) is the defining
rank count for a Johnson edge.  Equations (1.6)--(1.7) imply (1.8), and
Theorem 1.1 shows that the deficient windows cannot be changed by choosing
the split halves.  \(\square\)

The obstruction also explains the deadline issue.  The `d+1` old owner
occurrences whose source intervals contain `Q_p` have injective full-block
lifts, but those lifts have length `d+2`.  Thus OR equality survives while
the flat deadline does not.

## 2. Corrected sharp-source anchor table

Suppress the fixed core `K` and write the filler bank as
`F={f_0,...,f_(d+1)}`.  The internal anchors and the literal sharp source
letters are as follows.

### Phase zero

\[
\begin{array}{c|c|c}
\text{expanded anchor}&\text{sharp }p&Q_p\setminus K\\ \hline
L(6d+19)&6d+17&\{z,a_1,f_1\}\\
L(7d+22)&7d+20&\{a_3,f_0,f_1\}\\
L(8d+24)&8d+22&\{a_0,a_3,f_0\}\\
R(6d+16)&6d+14&\{f_d,f_{d+1}\}\\
R(7d+19)&7d+17&\{z,a_3,f_d\}\\
R(7d+20)&7d+18&\{z,f_{d+1}\}\\
R(7d+21)&7d+19&\{z,f_0\}.
\end{array}                                               \tag{2.1}
\]

### Phase one

\[
\begin{array}{c|c|c}
\text{expanded anchor}&\text{sharp }p&Q_p\setminus K\\ \hline
L(d+5)&d+3&\{f_1,f_2\}\\
L(d+6)&d+4&\{a_3,f_2,f_3\}\\
L(2d+7)&2d+5&\{z,a_3,f_1\}\\
L(3d+10)&3d+8&\{a_1,f_0,f_1\}\\
R(3d+7)&3d+5&\{z,a_1,f_d\}\\
R(3d+8)&3d+6&\{z,f_{d+1}\}\\
R(3d+9)&3d+7&\{z,f_0\}.
\end{array}                                               \tag{2.2}
\]

Phase zero has one exterior partition anchor, `L(1)`.  Phase one has two,
`L(1)` and `R(9d+25)`.  This gives the exact decompositions

\[
                         8=1+7,\qquad 9=2+7.             \tag{2.3}
\]

The earlier `7/8 internal` sentence arose by subtracting only the common
left exterior anchor in phase one.

## 3. Exact rank and adjacency refinement

For thirteen of the fourteen anchor rows, every forced middle window in
(1.5) has rank exactly `r-1`, and consecutive middle windows exchange one
coordinate in each direction.  Thus the forced valley is itself a
rank-`r-1` Johnson path of length `d`.

There is one sharper failure.  In phase zero at

\[
                         p=6d+14                         \tag{3.1}
\]

(the anchor `R(6d+16)`), the third forced middle window has rank `r-2`:

\[
 (|C_1|,\ldots,|C_d|)
   =(r-1,r-1,r-2,r-1,\ldots,r-1).                       \tag{3.2}
\]

The two incident changes have directed differences `(2,1)` and `(1,2)`, so
even the lower-rank sequence is not a Boolean Hasse path there.  These exact
claims are obtained directly from the eight-address sharp source formulas
and are replayed through `d=64`; the flat impossibility itself already
follows symbolically from Theorem 1.2.

## 4. Constraint-by-constraint conclusion

For every internal native ray anchor:

* **owner rank:** fails in `d` decomposition-independent windows;
* **Johnson legality:** consequently fails for a flat rank-`r` Johnson
  chronology; at the exceptional anchor (3.1), even the forced lower-rank
  valley has two non-Hasse joins;
* **deadline:** the canonical old owner witnesses crossing the host survive
  only as length-`d+2` full-block lifts, one beyond the old deadline;
* **residence:** the tested split words may retain the numerical run bound,
  but residence cannot repair the prior owner-rank failure; any admissible
  nonflat use still needs a separately proved boundary state;
* **common cap:** copying the old cap can contain `Z,T subseteq Q_p`, but this
  cannot repair the owner-rank or deadline failures;
* **recycling:** contraction is OR-exact, yet the expanded state is not an
  admissible flat state, so the native anchor cannot serve as a recyclable
  flat split host.

Hence the `8/9` native rays are occurrence geometry, not a ready internal
split-host atlas.  The remaining positive choices are genuinely different:
a planted exterior/two-sided host, a coordinated multi-position rethread
whose extra positions enter the deficient windows, or a nonflat compiler
which explicitly pays the `d+2` occurrences and proves its own residence and
matching state.

## 5. Replay

Run

```text
python3 scratch/audit_ad_octagon_internal_ray_flat_split_obstruction_20260801.py --write
```

The dependency-free replay checks `5<=d<=64`, both anchor coordinate maps,
all fourteen sharp letters, the universal intersection containment, every
forced middle rank, and every middle-window step.  Its finite depth range is
a regression audit; Theorem 1.2 is the all-`d` proof.

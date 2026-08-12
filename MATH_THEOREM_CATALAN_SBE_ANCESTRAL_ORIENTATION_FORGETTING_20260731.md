# SBE ancestral orientation forgetting and the exact newborn terminal-buffer cut

Date: 2026-07-31  
Status: dimension-uniform equivalence proved; the authenticated chained
`n=4 -> 5` step is completely audited and is orientation-forgetting.  No
all-parameter supply of absorbing newborn banks is claimed.

## 0. Result

Path orientation is a gauge variable for the strict balanced-expansion
(SBE) gate.  It does not change either shore's occurrence graph.  It only
chooses one terminal endpoint of each path for weight one; the two shores
choose complementary endpoints.  Consequently orientation is not a state
that must itself be preserved through the ancestral-face recursion.

There is an exact all-parameter criterion for a fixed orientation of the
newborn paths to absorb **every** orientation of all inherited paths.  If
`W` is an occurrence neighbourhood, the worst inherited orientation
contributes exactly the number of inherited path endpoint pairs wholly
contained in `W`.  Adding the selected newborn terminals gives the entire
worst-case weighted Hall row.

On the authenticated chained `n=4 -> 5` lift, the 28 stored newborn path
orientations satisfy this criterion for every orientation of the 14
inherited paths.  The same is true if every newborn path is instead
oriented toward its numerically smaller terminal, or every newborn path is
oriented toward its numerically larger terminal.  Thus this step is not
merely SBE-preserving: it is **orientation-forgetting and SBE-regenerating**.

The small cases show why this does not yet prove induction.  At `n=3` no
orientation is SBE on both shores.  At `n=4`, the two uniform endpoint
extremes fail on opposite shores, while exactly 7,600 of the `2^14`
advertised orientations pass.  A literal upper occurrence cut forces the
correlated clause

\[
                         x_4\mathbin\lor x_{13}.       \tag{0.1}
\]

Either one-path flip repairs the stored orientation, but no component is
individually forced.  The all-`n` missing theorem is therefore the supply
of a globally cut-compatible newborn terminal buffer, not preservation of
a previous `Q` or of previous path directions.

## 1. Orientation gauge

Fix a Catalan path forest `F` at parameter `n`.  Its child edges are the
unordered adjacent pairs along its paths.  For one shore let

\[
                         G_s=(O_s,X)
\]

be the strict occurrence graph.  Write

\[
 N=\binom{2n}{n-1},\qquad
 C=\binom{2n}{n}-\binom{2n}{n-2},\qquad
 R=N-C.
\]

For every path `P_j`, denote its two endpoints by `a_j,b_j`; they may be
equal for a singleton path.  Orienting `P_j` chooses its upper terminal to
be one of these endpoints.  Its lower terminal is the other endpoint.
Let `Z_s(x)` be the resulting terminal bank on shore `s`.

### Lemma 1.1 (exact gauge separation)

Reversing any collection of path components leaves unchanged:

1. the undirected forest and both child colour palettes;
2. both strict occurrence graphs `G_s` and all their adjacency sets;
3. component topology and every residence run length; and
4. the ancestral-face and source-ear counting identities.

It changes only the terminal bank `Z_s(x)`, hence the strict endpoint
pullback and the family of feasible strict common bases.

#### Proof

Each occurrence is computed from the lower intersection and upper union of
an adjacent pair.  Reversing that pair changes neither set, so every
occurrence edge and the whole occurrence graph are fixed.  Reversing a
path preserves its undirected edges, palettes, topology, and reverses each
coordinate word without changing run lengths.  The endpoint image contains
all vertices of a path except the final endpoint above and except the
initial endpoint below.  Thus only the complementary terminal choices
change.  The strict pulled-back matroids use those endpoint images, so
their common-basis families need not remain the same. `square`

This fixes the legal order of the recursive choices:

\[
 \boxed{\text{undirected output}\;\longrightarrow\;
        \text{orientation gauge}\;\longrightarrow\;Q\text{ and SDRs}.}
                                                               \tag{1.1}
\]

A gauge reset is legal before `Q` is chosen.  It is not legal to reorient
and silently retain an already frozen `Q` or its direct representatives.

## 2. The all-parameter ancestral-forgetting criterion

Suppose the components of `F` are partitioned into inherited paths `I`
and newborn paths `B`.  Fix an orientation `y` only on `B`, while allowing
the inherited orientation `x` to vary arbitrarily.

For an outer family `U subseteq O_s`, put

\[
 W_s(U)=N_{G_s}(U),                                   \tag{2.1}
\]

and define

\[
 p_{I,s}(W)=
   \#\{j\in I:\ a_j\in W\text{ and }b_j\in W\},     \tag{2.2}
\]

\[
 t_{B,s}(W;y)=|Z_{B,s}(y)\cap W|.                    \tag{2.3}
\]

The definition (2.2) also handles singleton paths: their repeated endpoint
contributes one exactly when it lies in `W`.

### Theorem 2.1 (newborn terminal-buffer equivalence)

The fixed newborn orientation `y` makes shore `s` SBE for **every**
orientation of all inherited paths if and only if, for every outer family
`U subseteq O_s`,

\[
\boxed{
 N|U|\ \le\ R|W_s(U)|+
 C\bigl(p_{I,s}(W_s(U))+t_{B,s}(W_s(U);y)\bigr).}
                                                               \tag{2.4}
\]

It makes both shores SBE for every inherited orientation if and only if
(2.4) holds on both shores, with the complementary newborn terminal
choices below.

#### Proof

The weighted SBE capacity of a neighbourhood `W` is

\[
 R|W|+C|Z_s(x,y)\cap W|,                              \tag{2.5}
\]

because endpoint-image vertices have weight `R` and terminals have weight
`N=R+C`.  On an inherited non-singleton path, orientation can select either
endpoint as the terminal.  The minimum possible contribution to `W` is one
if both endpoints lie in `W`, and zero otherwise.  Singleton paths obey the
same statement.  Choices on distinct paths are independent, so

\[
 \min_x |Z_s(x,y)\cap W|
   =p_{I,s}(W)+t_{B,s}(W;y).                           \tag{2.6}
\]

Substituting (2.6) into the weighted Hall inequality gives (2.4).  Since
this is done for every outer family, it is necessary and sufficient for
every inherited orientation.  Apply the same argument separately to the
two complementary shores. `square`

Call `y` an **absorbing newborn orientation** when it satisfies (2.4) on
both shores.  The theorem gives the exact recursive implication:

> If every strict lift admits an absorbing orientation of its newborn
> component bank, then SBE regenerates at every output regardless of all
> ancestral path orientations.  No orientation bits have to be carried in
> the inductive collar; they may be reset before choosing the new `Q`.

This is a dimension-free invariant, not yet a dimension-free construction.
The inequalities remain global occurrence cuts, and an absorbing `y` is
not proved to exist for every newborn bank.

## 3. Exact chained `n=4 -> 5` regeneration

The independent endpoint-orientation census gives the following exact
small data.

* At `n=3`, only three of the five path directions are effective and none
  of their eight assignments makes both shores SBE.
* At `n=4`, ten of the fourteen path directions are effective; four paths
  are singletons.  Exactly 475 of the `2^10` effective assignments pass,
  hence exactly `475*16=7,600` of the advertised `2^14` orientations pass.
* The stored `n=4` orientation has scaled violations `(14,0)`.  Reversing
  path 4, with endpoints `77,92`, or path 13, with endpoints `169,232`,
  gives `(0,0)`.

The ancestral-face identity embeds all 14 `n=4` paths literally as
`c+F_4` in the `n=5` forest and adds 28 newborn paths.  Exhaustive replay
of all `2^10=1,024` effective inherited orientations gives `(0,0)` on both
shores in every case when the newborn bank is fixed in any one of these
three ways:

\[
\begin{array}{c|r|r}
\text{newborn convention}&\text{inherited assignments}&\text{failures}\\ \hline
\text{stored}&1024&0\\
\text{upper terminal numerically smaller}&1024&0\\
\text{upper terminal numerically larger}&1024&0.
\end{array}                                           \tag{3.1}
\]

The four inherited singleton directions multiply each row by 16 without
changing it.  Thus each row covers all 16,384 advertised inherited
orientations.  In particular all 475 feasible effective `n=4` assignments
extend, but the stronger statement is true: the `n=5` newborn bank absorbs
even all 549 infeasible effective parent gauges.

As a separate robustness check, every orientation at Hamming distance at
most two from the stored full `n=5` gauge passes: respectively `1`, `42`,
and `861` assignments at radii zero, one and two.  This is not an assertion
about all `2^42` orientations.

The numerical endpoint conventions in (3.1) are finite deterministic
rules tied to the encoded fixture.  They are not claimed to be
coordinate-equivariant or to work for all parameters.  What is reusable
is the exact cut criterion (2.4).

## 4. Sharp correlation at `n=4`

The two uniform endpoint conventions fail in opposite directions:

\[
 \Delta(\text{all upper terminals maximal})=(14,0),
 \qquad
 \Delta(\text{all upper terminals minimal})=(0,14).   \tag{4.1}
\]

More sharply, let `x_i=1` mean that path `i` is reversed from the stored
orientation, so its initial endpoint becomes its upper terminal.  Take on
the upper shore all rank-six outer masks except `0x7d,0xed`.  Its
neighbourhood has order 67.  Twelve path endpoint pairs are wholly inside
the neighbourhood, only the initial endpoints of paths 4 and 13 are
additionally present, and no endpoint lies in the opposite one-sided
class.  Since `(N,R,C)=(56,14,42)`, its SBE row is

\[
 42\bigl(12+x_4+x_{13}\bigr)
   \ge 56\cdot26-14\cdot67=518,                       \tag{4.2}
\]

which is exactly the Boolean clause (0.1).  Both one-path repairs attain
it, and the complete census confirms that every feasible orientation
satisfies it.

Thus the orientation problem is a global signed Boolean cut system.  A
uniform per-path endpoint extremum is already too weak at `n=4`; the
correlation must be solved globally or supplied by an absorbing newborn
bank.  The `n=3` infeasibility shows that SBE itself cannot serve as an
unqualified base invariant from the first strict fixture.

## 5. Audit and scope

The new audit is

```text
scratch/audit_catalan_sbe_ancestral_orientation_forgetting_20260731.py
scratch/catalan_sbe_ancestral_orientation_forgetting_20260731.audit.json
```

It authenticates the chained witness and the independent `n=3/n=4`
orientation census, reconstructs the literal ancestral embedding, and
recomputes every stated `n=5` weighted min-cut.  Its canonical payload hash
at first freeze is

```text
fd9c3748559c2c5d8ad4352351aa18f20b54443d16defc95b2cf01039828f265
```

A clean-room cross-audit independently rebuilds the ancestral map, both
`n=5` occurrence graphs and all 1,024 min-cuts for each of the three
newborn conventions:

```text
scratch/independent_audit_catalan_sbe_n4_face_in_n5_20260731.py
  SHA b4f921568b6c5fdb3aa78fdcc205046ebc13b056d8c609fd82600a84620a6cb5
scratch/catalan_sbe_n4_face_in_n5_20260731.independent.audit.json
  SHA 7f4c6675e2f4bea83d1c0954fe69c6a78444c57df6926ed05b942d036a81d7fc
  payload 0996f6e46ae688d6f28635faaa80af3cb466c3d0c4397a3bbbfef847e5d87034
```

The exact scope is:

* The gauge-separation lemma and terminal-buffer equivalence are all-
  parameter theorems.
* Orientation is selected before `Q`; the set of common `Q` bases may
  change under a gauge reset.
* The orientation-forgetting certificate is finite for this authenticated
  `n=4 -> 5` chained lift.
* No absorbing newborn bank is constructed for arbitrary `n`, and no
  physical SDR, residence, deep-shadow, compiler, or `nu=B` conclusion is
  added here.

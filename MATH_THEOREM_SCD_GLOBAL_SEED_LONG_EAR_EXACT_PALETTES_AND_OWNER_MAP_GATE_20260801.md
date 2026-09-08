# The four-row SCD has an exact upper/lower seed; long ears reduce everything to four owner maps

Date: 2026-08-01  
Lane: explicit SCD absorber forest / tight one-to-two augmenter  
Status: unconditional exact seed arithmetic, exact missing-palette
assignment, exact lower-tail closure, and exact owner-map/graphic reduction.
Injective owner maps and all-`m` acyclicity are not proved.

## 0. Outcome

Put

\[
\begin{aligned}
 D&={2m-3\choose m-2},&
 E&={2m-3\choose m-3},&
 J&={2m-3\choose m-4},\\
 c&=D-E=\operatorname {Cat}_{m-1},&
 I_m&=E-J=\operatorname {Cat}_m-2c,&
 C&=\operatorname {Cat}_m=2D-E-J.
\end{aligned}                                       \tag{0.1}
\]

Here `D` is the number of central SCD chains `S<L` in `B_G`, `E` is the
number of long chains `R<S<L<U`, and `J` is the number of very long chains
which also contain `W>U` at rank `m+1`.

The four-row matching contains a literal isolated-edge seed:

* one `azL` provider `aL--azS` for every one of the `D` central chains;
* one `zU` provider `U--zL` for every one of the `E` long chains.

These `D+E` edges are pairwise resource-disjoint.  Since

\[
 W={2m-1\choose m}=3D+E,                            \tag{0.2}
\]

the seed has exactly `2D` components.  It covers every `az`-upper and
every `z`-only upper.  Its missing palette is exactly

\[
 \boxed{
 \mathcal M=left\{aU:U\in{G\choose m}\right\}
 \mathbin{\dot\cup}{G\choose m+1}, }
                                                               \tag{0.3}
\]

of order

\[
                         s=E+J=2D-C.                \tag{0.4}

There is a canonical distinct switch for every target in (0.3).

* For each long `R<S<L<U`, augment its `azL` provider to add `aU`.
* For each very long `R<S<L<U<W`, augment its `zU` provider to add `W`.

The `s` switches are distinct.  Each adds one edge and lowers the component
count by one, so if their new owner heads are injective and their union is
acyclic, the result has

\[
                         2D-s=C                    \tag{0.5}

components, exactly as an upper-exact owner forest must.

More strongly, use the fixed-`M_0` deletion choices from the SCD chains.
Then the final candidate uses every upper colour exactly once and every
selected lower/tail resource exactly once.  Exactly `C` lower resources
remain unused.  Thus the palette and scalar rows close *without* a nibble,
DP theorem, or post-hoc compiler.

The entire remaining owner-layer problem is four explicit cross-facet
maps.  In the standard Greene--Kleitman SCD these maps have large fibres:
finite exact audits through `m=9` give maximum indegree and physical degree
`m-1`, although the resulting support is acyclic in every audited case.
Hence the canonical candidate is an exact upper/lower rainbow branching
forest, not yet a cap-two linear forest.

## 1. The isolated seed

Write

\[
 [2m-1]=G\mathbin{\dot\cup}\{a,z\},\qquad |G|=2m-3.
\]

For a central chain, use the notation

\[
 R\subset S\subset L\subset U\subset W,             \tag{1.1}
\]

omitting `R,U,W` when the chain does not reach their ranks.  The four-row
matching is

\[
\begin{array}{c|cc}
\text{lower root}&\text{long chain}&\text{short chain}\\ \hline
azR&azS&-\\
zS&zL&azS\\
aS&aL&aL\\
L&U&zL.
\end{array}                                         \tag{1.2}
\]

For every central chain select the physical edge

\[
                         aL--azS                    \tag{1.3}

of lower colour `aS` and upper colour `azL`.  In rooted form it is

\[
 aS\to\begin{cases}
        azR,&\text{long},\\
        zS,&\text{short}.
       \end{cases}                                  \tag{1.4}

For every long chain also select

                         U--zL                      \tag{1.5}

of lower colour `L`, upper colour `zU`, and rooted form `L->zS`.

### Theorem 1.1 (exact SCD seed)

The edges (1.3)--(1.5) are pairwise disjoint in lower resources, rooted
tail/head roles, physical owners, and upper colours.  They form a matching
and hence a physical linear forest of `D+E` isolated edges.

They cover the complete upper sectors

\[
                         az{G\choose m-1},
 \qquad                  z{G\choose m}.             \tag{1.6}

#### Proof

The `D` central chains use every rank-`(m-1)` `L subset G` once, and the
`E` long chains use every rank-`m` `U subset G` once.  Their four physical
owner banks have signatures `a`, `az`, empty, and `z`, respectively, so
they are cross-disjoint; within a signature the SCD members are injective.
The rooted lower banks in (1.4)--(1.5) have distinct signatures or belong
to disjoint short/long chain classes.  This proves the matching statement
and (1.6). \(\square\)

The rank-`(m+1)` upper layer splits by `{a,z}` signature as

\[
 {G\choose m+1}
 \mathbin{\dot\cup}a{G\choose m}
 \mathbin{\dot\cup}z{G\choose m}
 \mathbin{\dot\cup}az{G\choose m-1}.                \tag{1.7}

Its sector orders are `J,E,E,D`, proving (0.3)--(0.4).

## 2. The long `aU` ear

Fix a long central chain and name its three central increments

\[
                         S=R+\rho,
 \qquad                  L=S+x,
 \qquad                  U=L+y.                    \tag{2.1}

Apply the tight augmenter to the seed edge `aL--azS` with

\[
 \widehat L=aS,qquad
 \widehat a=x,qquad
 \widehat b=y,qquad
 \widehat c=z,qquad
 \widehat x=\rho.                                   \tag{2.2}

Then

\[
\begin{array}{lll}
 \widehat A=aL,&
 \widehat B=a(S+y),&
 \widehat C=azS,\\
 \widehat L'=azR,&
 \widehat D=az(R+x),&
 \widehat R=aU.
\end{array}                                         \tag{2.3}

The fixed-phase rows are exact:

\[
 M_0(aS)=aL,qquad M_0(azR)=azS.                   \tag{2.4}

Thus the rooted replacement is

\[
\boxed{
 aS\to azR\ [azL]
 \rightsquigarrow
 aS\to M_0^{-1}(a(S+y))\ [aU]
 +azR\to M_0^{-1}(az(R+x))\ [azL]. }
                                                               \tag{2.5}

It retains lower `aS`, consumes the previously unused lower `azR`, retains
the old colour `azL`, and adds the missing colour `aU`.

Every rank-`m` `U subset G` occurs in exactly one long SCD chain, so (2.5)
assigns all `E` missing `a`-only colours to distinct auxiliary switches.

## 3. The very-long all-`G` ear

Now assume the chain continues

\[
                         W=U+v.                     \tag{3.1}

Apply the tight augmenter to the seed edge `U--zL` with

\[
 \widehat L=L,qquad
 \widehat a=y,qquad
 \widehat b=v,qquad
 \widehat c=z,qquad
 \widehat x=x.                                      \tag{3.2}

Then

\[
\begin{array}{lll}
 \widehat A=U,&
 \widehat B=L+v,&
 \widehat C=zL,\\
 \widehat L'=zS,&
 \widehat D=z(S+y),&
 \widehat R=W.
\end{array}                                         \tag{3.3}

Again the fixed-phase rows are exact:

\[
 M_0(L)=U,qquad M_0(zS)=zL.                       \tag{3.4}

The rooted replacement is

\[
\boxed{
 L\to zS\ [zU]
 \rightsquigarrow
 L\to M_0^{-1}(L+v)\ [W]
 +zS\to M_0^{-1}(z(S+y))\ [zU]. }
                                                               \tag{3.5}

It retains lower `L`, consumes lower `zS`, retains `zU`, and adds the
missing all-`G` colour `W`.

Every rank-`(m+1)` `W subset G` occurs in one SCD chain and has a distinct
rank-`m` predecessor `U`, so the `J` targets in (3.5) use distinct seed
switches.

The deletion choices in (2.2) and (3.2) are important.  Choosing `a`
instead of `rho` in (2.2) and `x` in (3.2) would use lower `zS` twice.
The fixed-phase choices use `azR` and `zS`, respectively, and therefore
close the lower palette exactly.

## 4. Exact upper and lower closure

Apply (2.5) on all `E` long chains, and (3.5) on all `J` very long chains.
The chain types contribute:

\[
\begin{array}{c|c|c|c}
\text{chain type}&\text{number}&\text{final edges}&\text{used lower rows}\\ \hline
\text{short}&c&1&aS\\
\text{long, ending at }U&I_m=E-J&3&aS,azR,L\\
\text{very long, reaching }W&J&4&aS,azR,L,zS.
\end{array}                                         \tag{4.1}

### Theorem 4.1 (exact palette candidate)

The resulting family has

\[
 \boxed{
 c+3I_m+4J
 =D+2E+J
 ={2m-1\choose m+1}=W-C }                           \tag{4.2}

edges.  Its upper colours are all distinct and equal the complete
rank-`(m+1)` layer.  Its lower/tail resources are all distinct.  The unused
lower resources are exactly

* `zS` on the `I_m` long chains ending at `U`; and
* `L,zS` on the `c` short chains.

Their number is

\[
                         I_m+2c=C.                  \tag{4.3}

#### Proof

The four upper signature sectors are supplied respectively by (3.5),
(2.5), the retained/rerouted `zU` edges, and the retained/rerouted `azL`
edges.  Signature separates the sectors and the SCD indexes each member of
a sector uniquely.  The lower rows in (4.1) are disjoint by signature and
chain membership.  Equations (0.1) give (4.2)--(4.3). \(\square\)

Thus there is no remaining upper-colour, lower-colour, scalar, or switch-
assignment problem.  Only owner/head capacity and forest topology remain.

## 5. The four owner maps

Every old physical owner resource survives an augmentation.  The only new
owners are the following cross facets:

\[
\begin{array}{c|c|c}
\text{map}&\text{domain}&\text{new owner}\\ \hline
\beta_a&\text{long chains}&a(S+y)\\
\delta_a&\text{long chains}&az(R+x)\\
\beta_0&\text{very long chains}&L+v\\
\delta_0&\text{very long chains}&z(S+y).
\end{array}                                         \tag{5.1}

Their `{a,z}` signatures are pairwise distinct.  Inside one row, equality
of new owners is exactly equality of the corresponding rooted heads under
the bijection `M_0^{-1}`.

Moreover every image owner is already in the matching's complete owner
palette:

* `a(S+y)` is some `aL'`;
* `az(R+x)` is some `azS'`;
* `L+v` is some rank-`m` owner `U'`;
* `z(S+y)` is some `zL'`.

It therefore lands on an old endpoint of another seed/ear component.  One
preimage gives physical degree two and joins two pieces; repeated preimages
give degree at least three.

### Theorem 5.1 (exact linear-forest gate)

The palette candidate of Theorem 4.1 is a rooted/physical linear forest if
and only if

1. each of the four maps in (5.1) is injective; and
2. the directed graph formed by the rooted arcs in (1.4)--(1.5),
   (2.5), and (3.5) has no directed cycle.

When these conditions hold, it has exactly `C` path components.

#### Proof

Every lower/tail is distinct by Theorem 4.1, so outdegree is at most one.
The four signature classes in (5.1) cannot collide with each other.
Within a class, injectivity is exactly head indegree at most one.  Because
each image owner is an already used endpoint, the same condition is
equivalent to physical degree at most two.  A finite graph of maximum
indegree and outdegree one is a disjoint union of paths and cycles; hence
condition 2 is exactly acyclicity.  Finally `W` vertices and `W-C` forest
edges give `C` components. \(\square\)

This is the promised exact owner-map collision/forest graph.  It is much
smaller than the original four-resource selector: the complete palette and
lower rows have disappeared from the search.

## 6. What the standard Greene--Kleitman choice does

The deterministic audit

`scratch/audit_scd_global_seed_long_ears_20260801.cpp`

constructs the standard SCD, its four-row matching, and the literal ears
(2.5), (3.5).  It verifies upper and lower closure exhaustively.  For
`m=3,...,9` it reports:

\[
\begin{array}{c|rrrrrrr}
m&3&4&5&6&7&8&9\\ \hline
\max\deg^-&2&3&4&5&6&7&8\\
\max\deg_{\rm phys}&2&3&4&5&6&7&8\\
\text{undirected cycles}&0&0&0&0&0&0&0.
\end{array}                                         \tag{6.1}

The repeated-image counts `|domain|-|image|` are

\[
\begin{aligned}
 \operatorname {coll}(\beta_a)
 =\operatorname {coll}(\delta_a)
 &= {2m-4\choose m-4},\\
 \operatorname {coll}(\beta_0)
 =\operatorname {coll}(\delta_0)
 &= {2m-4\choose m-5}
\end{aligned}                                       \tag{6.2}

through the audited range.  Equation (6.2) is recorded as an audited
pattern, not used as an all-`m` theorem here.

Thus the canonical SCD already appears to solve the graphic row but fails
the degree row linearly.  The required repair is a **cross-facet
detachment**: reassign the provider facet and/or deletion coordinate for
each target so that all four maps become injective while preserving the
exact lower rows and acyclicity.

## 7. Sharpened remaining theorem

The previous global target asked for a protected upper-exact Catalan forest
inside a large diamond selector.  The SCD seed reduces it to:

> **SCD cross-facet detachment lemma.**  Reassign the `E` long `aU` ears
> and `J` very-long `W` ears among legal SCD provider occurrences so that
> the four owner maps are injective, the lower tails still form a
> complement of size `C`, and the directed owner graph remains acyclic.

Any proof of this lemma gives an explicit upper/lower-exact physical linear
forest with exactly `C` components.  The separate rooted connector braid,
protected pivot, residence, deeper upper shadows and common cap would still
have to be installed, but the formerly opaque upper-colour selector would
be replaced by a literal recursive SCD absorber forest.

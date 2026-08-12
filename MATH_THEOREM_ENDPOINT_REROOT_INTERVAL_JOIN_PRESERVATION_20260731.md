# Endpoint reroots preserve block-internal interval joins

Date: 2026-07-31  
Status: proved in every join-semilattice; the genuine-fourfilter `c7be` chronology is an exact audited example

## 1. Setting

Let \((L,\vee)\) be a join-semilattice and let

\[
X=(x_0,\ldots,x_{n-1})
\]

be a finite nonempty sequence.  For a nonempty interval write

\[
J_X(i,j)=\bigvee_{k=i}^j x_k,
\qquad
\mathcal C(X)=\{J_X(i,j):0\le i\le j<n\}.
\]

For a nonempty block \(B=(b_0,\ldots,b_{m-1})\), put

\[
\begin{aligned}
P(B)&=\left\{\bigvee_{i=0}^j b_i:0\le j<m\right\},\\
S(B)&=\left\{\bigvee_{i=j}^{m-1}b_i:0\le j<m\right\},\\
W(B)&=\bigvee_{i=0}^{m-1}b_i.
\end{aligned}
\]

For families \(A,D\subseteq L\), write

\[
A\vee D=\{a\vee d:a\in A,\ d\in D\}.
\]

No distributivity, complement, rank, or Boolean representation is used below.
Finiteness of \(L\) is needed only if one wants to enumerate all targets.

## 2. Exact oriented-block formula

### Lemma 2.1 (one block)

For every block \(B\),

\[
\mathcal C(\operatorname{rev}B)=\mathcal C(B),\qquad
P(\operatorname{rev}B)=S(B),\qquad
S(\operatorname{rev}B)=P(B).
\tag{2.1}
\]

#### Proof

Reversal bijects intervals of \(B\) with intervals of \(\operatorname{rev}B\).
Their entries appear in reverse order, but a join is commutative and
associative.  A prefix of the reversed block is a reversed suffix of the
original block, and conversely. ∎

### Theorem 2.2 (arbitrarily many disjoint reversals)

Partition the original sequence into consecutive nonempty blocks

\[
X=B_1\Vert B_2\Vert\cdots\Vert B_m.
\]

Choose an orientation \(\epsilon_i\in\{+,-\}\) for each block and concatenate
the blocks in the same order, reversing precisely those with sign \(-\).  Put

\[
L_i^{+}=P(B_i),\quad R_i^{+}=S(B_i),\qquad
L_i^{-}=S(B_i),\quad R_i^{-}=P(B_i).
\tag{2.2}
\]

Then the complete interval-join coverage of the oriented concatenation is

\[
\boxed{
\bigcup_{i=1}^m\mathcal C(B_i)
\;\cup\!
\bigcup_{1\le p<q\le m}
R_p^{\epsilon_p}\vee
\{W(B_{p+1})\vee\cdots\vee W(B_{q-1})\}\vee
L_q^{\epsilon_q}.}
\tag{2.3}
\]

When \(q=p+1\), the middle factor in (2.3) is omitted.  Formula (2.3)
therefore handles any collection of pairwise-disjoint prefix, suffix, or
interior reversals after cutting at all their endpoints.

#### Proof

An interval lies either inside one oriented block or crosses a unique first
block \(p\) and last block \(q\).  In the latter case it consists of a suffix
of the oriented block \(p\), every whole intermediate block, and a prefix of
the oriented block \(q\).  Lemma 2.1 gives exactly the families in (2.2).
Conversely, every choice in the displayed family is realized by the
corresponding interval. ∎

### Corollary 2.3 (one endpoint cut)

For \(X=A\Vert B\), let

\[
I=\mathcal C(A)\cup\mathcal C(B).
\]

Then

\[
\begin{aligned}
\mathcal C(A\Vert B)&=I\cup(S(A)\vee P(B)),\\
\mathcal C(\operatorname{rev}A\Vert B)&=I\cup(P(A)\vee P(B)),\\
\mathcal C(A\Vert\operatorname{rev}B)&=I\cup(S(A)\vee S(B)).
\end{aligned}
\tag{2.4}
\]

Thus, for example, a prefix reroot loses exactly

\[
(S(A)\vee P(B))\setminus\bigl(I\cup(P(A)\vee P(B))\bigr)
\tag{2.5}
\]

and gains exactly the same expression with the two cross-families exchanged.
This is an equality, not a relaxation.

### Corollary 2.4 (two endpoint reroots)

For \(X=A\Vert B\Vert C\), the old cross-block family is

\[
(S(A)\vee P(B))\cup(S(B)\vee P(C))
\cup(S(A)\vee\{W(B)\}\vee P(C)),
\tag{2.6}
\]

whereas the cross-block family of
\(\operatorname{rev}A\Vert B\Vert\operatorname{rev}C\) is

\[
(P(A)\vee P(B))\cup(S(B)\vee S(C))
\cup(P(A)\vee\{W(B)\}\vee S(C)).
\tag{2.7}
\]

The internal family
\(\mathcal C(A)\cup\mathcal C(B)\cup\mathcal C(C)\) is common to both.

## 3. The exact adjacent-boundary ledger

Let \(Y\) be obtained from \(X\) by reversing the inclusive segment
\([a,b]\).  Let \(m_X(t)\) be the multiplicity of \(t\) among the adjacent
joins \(x_i\vee x_{i+1}\).  All internal adjacent pairs of the reversed block
are merely traversed backwards.  Hence

\[
\begin{aligned}
m_Y(t)=m_X(t)
&-\mathbf 1_{a>0}[x_{a-1}\vee x_a=t]
-\mathbf 1_{b<n-1}[x_b\vee x_{b+1}=t]\\
&+\mathbf 1_{a>0}[x_{a-1}\vee x_b=t]
+\mathbf 1_{b<n-1}[x_a\vee x_{b+1}=t].
\end{aligned}
\tag{3.1}
\]

A prefix or suffix reroot has only one changed cut.  Thus a required adjacent
colour survives exactly when its right side in (3.1) is positive.  In
particular, removing one occurrence of a colour of old multiplicity at least
two is safe, and a formerly missing colour is installed when it occurs among
the added boundary joins.  Coincident removed and added colours are handled
correctly by the full signed ledger (3.1).

For several disjoint reversals one may sum the signed cut contributions when
their cuts are distinct.  Formula (2.3), rather than an informal sum, remains
the fail-safe statement when blocks touch.

## 4. Preservation and installation certificates

### Theorem 4.1 (stable-witness preservation)

Let \(\Omega\subseteq L\) be a target family and partition \(X\) into the
blocks used by a proposed collection of disjoint reversals.  If

\[
\Omega\cap\mathcal C(X)
\subseteq
\bigcup_i\mathcal C(B_i),
\tag{4.1}
\]

then every previously covered target in \(\Omega\) remains covered after any
independent choice of block orientations.

If a missing family \(M\subseteq\Omega\setminus\mathcal C(X)\) is contained
in the new cross-block family of (2.3), then the new chronology covers

\[
(\Omega\cap\mathcal C(X))\cup M.
\tag{4.2}
\]

In particular, if \(\Omega\setminus\mathcal C(X)=M\), the reroot is complete
on \(\Omega\).

#### Proof

Every witness certified by (4.1) lies in one block.  Lemma 2.1 transports it
through reversal of that block without changing its join.  Every member of
\(M\) has a literal new crossing witness by (2.3). ∎

Condition (4.1) is deliberately strong and easy to audit.  The exact weaker
condition is obtained by replacing its right side with the union of the
internal family and the new cross-family in (2.3).

### Proposition 4.2 (targetwise endpoint trace)

Write \(u\le t\) when \(u\vee t=t\).  A target \(t\) belongs to
\(\mathcal C(X)\) if and only if some maximal consecutive run of entries
\(\le t\) has join \(t\).

Consequently, for a prefix cut \(A\Vert B\), if \(t\) has no witness wholly
inside \(A\) or \(B\), then:

- before rerooting, \(t\) is covered exactly when the maximal
  \(t\)-compatible suffix of \(A\) joined with the maximal compatible prefix
  of \(B\) equals \(t\);
- after reversing \(A\), replace that suffix of \(A\) by its maximal
  compatible prefix.

The suffix statement is symmetric.  This gives a linear scan per target and
shows precisely why only endpoint traces can alter a target that lacks an
internal witness.

#### Proof

Every cell in an interval of join \(t\) lies below \(t\).  Extending that
interval through adjacent cells below \(t\) cannot raise its join above
\(t\), and because the old join was already \(t\), the maximal compatible
run still joins to \(t\).  The converse is immediate. ∎

### Corollary 4.3 (seam-shadow rectangle)

At a new seam \(U\Vert V\), write the oriented entries as
\(U=(u_0,\ldots,u_{r-1})\) and \(V=(v_0,\ldots,v_{s-1})\).  Every value

\[
Q_{h,k}=
\left(\bigvee_{i=r-1-h}^{r-1}u_i\right)
\vee
\left(\bigvee_{j=0}^{k}v_j\right),
\qquad 0\le h<r,\ 0\le k<s,
\tag{4.3}
\]

is installed by a literal interval through the seam.  The base value
\(Q_{0,0}\) is the new adjacent boundary join; increasing \(h\) or \(k\)
gives its monotone seam shadows.  Therefore (4.1), the signed adjacent ledger,
and a short list of values from (4.3) are sufficient for a completely
solver-free endpoint-reroot certificate.

The shadow sequence need not grow strictly and need not move one rank at a
time.  Those stronger properties require separate hypotheses.

## 5. Worked example: the genuine-fourfilter `c7be` chronology

The authenticated natural K16 target chronology is

```text
scratch/k16_true_fourfilter_natural_targets_20260731.word
SHA-256 0f6d64e9311ef634169964350baa8f817b17b9d1619970c881f87e7346550a5c
```

Partition it into the half-open blocks

\[
A=[0,6389),\qquad B=[6389,12826),\qquad C=[12826,12870).
\tag{5.1}
\]

The endpoint-reroot chronology is exactly

\[
T^*=\operatorname{rev}A\Vert B\Vert\operatorname{rev}C
\tag{5.2}
\]

and is frozen as

```text
scratch/k16_true_fourfilter_endpoint_reroot_targets_20260731.word
SHA-256 c7beccc38489ad0ce4f203fa11e348a9fb04a18418cdc8ac9dce038ddde06906
```

### 5.1 Old coverage is block-stable

Exact interval replay gives

\[
|\mathcal C(T)|=39197
\]

and, more strongly,

\[
\mathcal C(T)
=\mathcal C(A)\cup\mathcal C(B)\cup\mathcal C(C).
\tag{5.3}
\]

The individual block spectra have sizes \(22684,16400,274\); their union is
all 39,197 old values.  Thus Theorem 4.1 proves before any new-spectrum
enumeration that no old interval-OR target can be lost by these two endpoint
reroots.

### 5.2 The signed q1 ledger

The two changed seams have the exact ledger

| seam | removed join | old multiplicity | added join | old multiplicity |
|---|---:|---:|---:|---:|
| prefix | `0xc3ce` | 2 | `0xd3cc` | 0 |
| suffix | `0xf38c` | 2 | `0xb3cc` | 0 |

After rerooting, all four displayed colours have multiplicity one.  Hence the
two old colours survive and the two missing adjacent colours are installed.

### 5.3 Six installed seam shadows

The two seam-shadow rectangles provide the following inclusive witnesses:

| target | interval in \(T^*\) |
|---|---:|
| `0xd3cc` | `[6388,6389]` |
| `0xd3ce` | `[6387,6389]` |
| `0xdbce` | `[6386,6389]` |
| `0xb3cc` | `[12825,12826]` |
| `0xf3cc` | `[12824,12826]` |
| `0xfbce` | `[12824,12828]` |

These are exactly the six masks missing from the old rank-at-least-eight
spectrum.  Exact application of (2.3), independently checked by an ending-OR
replay, gives

\[
\mathcal C(T^*)\setminus\mathcal C(T)
=\{\mathtt{b3cc,d3cc,d3ce,dbce,f3cc,fbce}\},
\qquad
\mathcal C(T)\setminus\mathcal C(T^*)=\varnothing.
\tag{5.4}
\]

Thus \(|\mathcal C(T^*)|=39203\), the entire Boolean rank-8-through-rank-16
tower.  The upper-completeness part of the genuine-fourfilter construction is
therefore a direct instance of Theorem 4.1 plus the six-row seam certificate,
not a solver-dependent phenomenon.

## 6. Audit artifacts and scope

```text
scratch/audit_k16_endpoint_reroot_join_preservation_20260731.py
SHA-256 968ecd20a0b95eeb2ebaa1dbff7a3c4e45216fabdd5eedfddd8b6138bd2dbf31

scratch/k16_endpoint_reroot_join_preservation_20260731.audit.json
SHA-256 59a891a5ed0df96e9ccde8a44cf5a79d76c45f618ecfb720eedfb56983a209d9
payload SHA-256 b92d600f5f8da35f4a46638b2566e2eea10074812eef1c2fe1dcddeace28424e
```

The replay authenticates both target files, checks the full adjacent-join
counter identity, reconstructs both spectra in two ways, verifies (5.3), and
checks every displayed seam witness.

This theorem concerns target chronology and contiguous joins.  It does not by
itself produce physical lower cells, a common-cap matching, or a literal
universal word.  Conversely, its abstract statements are not K16-specific:
they apply unchanged to any finite join-semilattice and any set of disjoint
block reversals.

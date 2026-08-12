# The c7be inert/singleton common-Q normal form

Date: 2026-07-31  
Status: exact conditional normal form and independently audited census; no common-Q solution claimed  
Scope: target SHA c7beccc38489..., the displayed P/Q schedule, and the fixed 0x8000 pin

## 1. Fixed data and definitions

Let $E=(E_p)_{p=0}^{12872}$ be the nonzero maximal middle envelope after
the already-audited cap $E_{6389}:=\mathtt{0x8000}$. Let
$\mathcal C$ be the exact physical lower-cell catalog of 32,230 intervals.
The prescribed middle rows are $(T_i,I_i)$, where

$$
   \bigvee_{p\in I_i}E_p=T_i.
$$

For a nonempty lower target $U$, put

$$
 \mathcal C_U^0=
 \left\{J\in\mathcal C:\bigvee_{p\in J}E_p=U\right\}.
$$

Call $U$ **inert** when $\mathcal C_U^0\ne\varnothing$, and let
$\mathcal I$ be the inert family. Let $\mathcal N$ be the remaining
lower targets. The superscript zero is important: an inert occurrence is
an occurrence in the fixed base envelope, before any new singleton caps.

Choose one retained base occurrence $J_U\in\mathcal C_U^0$ for every
$U\in\mathcal I$. Define the protected occurrence family

$$
 \mathcal P=
 \{(T_i,I_i):0\le i<12870\}
 \cup\{(U,J_U):U\in\mathcal I\}.
$$

For every $(D,J)\in\mathcal P$ and every bit $b\in D$, orient one
witness to a position

$$
 a(D,J,b)\in J,\qquad b\in E_{a(D,J,b)}.
$$

All bits of one inert target must be oriented inside the same chosen
interval $J_U$. Set

$$
 R_p=\{b:a(D,J,b)=p\text{ for some }(D,J)\in\mathcal P\}.
$$

Let $B$ contain the positions whose chosen inert occurrence is a
singleton. For a fixed orientation $a$, form a bipartite graph with left
side $\mathcal N$, right side the legal singleton catalog positions outside
$B$, and edge

$$
 S\sim_a p
 \quad\Longleftrightarrow\quad
 \{p\}\text{ is an exact individual candidate for }S,\quad
 S\subseteq E_p,\quad R_p\subseteq S.                       \tag{1.1}
$$

The individual-candidate clause is redundant once all protected traces are
represented in $R_p$, but retaining it is a safe and useful prefilter.

## 2. Exact oriented-anchor theorem

**Theorem 2.1.** Fix the base inert occurrences $J_U$ and a witness
orientation $a$. If $G_a$ has a matching $f$ saturating $\mathcal N$, define

$$
 A_p=
 \begin{cases}
 S,&f(S)=p,\\
 E_p,&p\notin f(\mathcal N).
 \end{cases}                                                \tag{2.1}
$$

Then every $A_p$ is nonzero, every prescribed middle row remains exact,
every chosen inert occurrence remains exact, and every lower target occurs.

### Proof

For a matched position $p=f(S)$, (1.1) gives $S\subseteq E_p$, so the
singleton cap is exactly $A_p=E_p\cap S=S\ne\varnothing$. At an unmatched
position $A_p=E_p\ne\varnothing$. Thus always $A_p\subseteq E_p$.

Fix a protected occurrence $(D,J)$. Since
$\bigvee_{p\in J}E_p=D$, every $E_p$ with $p\in J$ is a subset of $D$;
hence

$$
 \bigvee_{p\in J}A_p\subseteq D.                            \tag{2.2}
$$

For each $b\in D$, let $q=a(D,J,b)$. If $q$ is unmatched, then
$b\in E_q=A_q$. If $q=f(S)$, then $b\in R_q\subseteq S=A_q$.
Every bit of $D$ therefore survives somewhere in $J$, giving equality
in (2.2). This proves all middle and retained-inert equations. Finally,
every $S\in\mathcal N$ occurs on its matched singleton, and every
$U\in\mathcal I$ occurs on $J_U$. Hence all lower targets occur.

For a proposed singleton matching $f$, define

$$
 H_{D,J,b}=\{p\in J:b\in E_p\},\qquad
 Z_b(f)=\{f(S):S\in\mathcal N,\ b\notin S\}.
$$

The protected occurrence $(D,J)$ remains exact precisely when

$$
 H_{D,J,b}\not\subseteq Z_b(f)
 \quad\text{for every }b\in D.                              \tag{2.3}
$$

Choosing $a(D,J,b)$ is exactly choosing one member of
$H_{D,J,b}\setminus Z_b(f)$. Thus the bit-trace form (2.3) and the
witness-load form $R_{f(S)}\subseteq S$ are equivalent.

For fixed $a$, the exact oriented-anchor Hall condition is

$$
 |\mathcal F|
 \le
 \left|\bigcup_{S\in\mathcal F}
 \{p:S\sim_a p\}\right|
 \quad\text{for every }\mathcal F\subseteq\mathcal N.       \tag{2.4}
$$

By Hall's theorem, (2.4) is necessary and sufficient for the matching in
Theorem 2.1. With variable retained occurrences and orientations, the exact
condition for this normal form is

$$
 \exists (J_U)_{U\in\mathcal I}\;
 \exists a\;
 \forall\mathcal F\subseteq\mathcal N:\ (2.4).              \tag{2.5}
$$

This is an exact solver-free reduction, not a claim that one arbitrary or
greedy orientation satisfies Hall. Here "oriented" means the full
bit-witness orientation encoded by the loads $R_p$. The weaker endpoint-key
lemma for nested intervals is only a necessary antichain condition and is
not sufficient for common-Q.

## 3. Converse and the meaning of automatic

Consider words restricted to the singleton normal form (2.1). Suppose all
middle rows are exact and every inert target retains one of its
**base-inert** occurrences $J_U\in\mathcal C_U^0$. Choose, for each
required bit, any position where that bit survives in the final word.
These choices define an orientation $a$. At a matched position $p=f(S)$,
every designated bit belongs to $A_p=S$, so $R_p\subseteq S$; hence $f$
is a matching in $G_a$. Thus (2.5) is also necessary within this stated
normal form.

The inert intervals need no matching among themselves. Two distinct inert
targets cannot select the same base cell, since that cell has one fixed OR
label. Overlap of two distinct intervals is harmless. If $J_U=\{p\}$, then
$R_p\supseteq U$; together with $R_p\subseteq S\subseteq E_p=U$, this would
force $S=U$, impossible for $S\in\mathcal N$. Consequently the explicit
singleton reservation in (1.1) is logically automatic once all bits of $U$
are anchored, though keeping it makes the graph clearer.

What is **not** automatic is survival from the inert classification alone.
There is a literal c7be counterexample:

~~~text
E[8123] = 0x009e
E[8124] = 0x008f
base inert occurrence [8123,8125) has OR 0x009f

cap 0x009a at singleton 8123
cap 0x008b at singleton 8124
final OR on [8123,8125) = 0x009b
~~~

The two singleton targets are non-inert, the two caps cause zero middle-row
failures, but together they erase bit 0x0004 from the inert occurrence.
The witness-load condition blocks this pair by orienting that bit to at
least one of the two positions.

The base-occurrence qualifier is also load-bearing. If one merely requires
an arbitrary final occurrence $J$ with $\bigvee_JA=U$, while
$\bigvee_JE$ may strictly contain $U$, positive bit witnesses do not force
deletion of the extra base bits. Theorem 2.1 is sufficient, and the converse
is exact, for retained members of $\mathcal C_U^0$.

## 4. Upper completion and the missing chain hypothesis

Middle-row preservation alone does not generally preserve upper targets.
It does so here because two independent hypotheses hold:

1. every upper target $V$ is the OR of a consecutive middle block
   $T_i,\ldots,T_j$; and
2. the corresponding physical row intervals form one connected chain.

Indeed, if $I_i\cup\cdots\cup I_j=[\ell,r]$, then

$$
 \bigvee_{p=\ell}^{r}A_p
 =\bigvee_{k=i}^{j}\bigvee_{p\in I_k}A_p
 =\bigvee_{k=i}^{j}T_k=V.                                  \tag{4.1}
$$

For the c7be schedule the exhaustive target-order upper audit has zero
holes, and the monotone row schedule has zero chain breaks. Thus Theorem 2.1
plus oriented Hall produces a universal word. Without these two facts, one
must protect explicit physical upper occurrences as additional anchored
rows or perform a separate full upper replay.

## 5. Independent c7be census

The fixed pinned-envelope classification gives exactly

~~~text
inert       22494
non-inert    3838
~~~

with rank split

| rank | inert | non-inert |
|---:|---:|---:|
| 1 | 1 | 15 |
| 2 | 0 | 120 |
| 3 | 0 | 560 |
| 4 | 0 | 1820 |
| 5 | 3045 | 1323 |
| 6 | 8008 | 0 |
| 7 | 11440 | 0 |

The inert count includes 0x8000, which is inert relative to the
**already-pinned** envelope; making that pin was itself a nontrivial cap.
Thus 22,493 further lower targets are cap-free relative to the pinned base.

Before the variable inert witness loads are imposed, the exact
middle-protected singleton graph on the 3,838 non-inert targets has 168,592
incidences, minimum target degree 8, zero isolated targets, and a matching
of size 3,838. This is only a marginal precheck. Distinct individually legal
singleton caps can jointly erase all carriers of a protected bit, which is
precisely what (1.1)-(2.5) prevent.

Frozen independent census:

~~~text
scratch/audit_k16_c7be_inert_singleton_normal_form_20260731.py
  SHA-256 1a4b0e0a1f8f340d95fa0cfd3bd638a77fb6462691252ca7a93342c419b9ec4d
scratch/k16_c7be_inert_singleton_normal_form_20260731.audit.json
  SHA-256 eea1319a1d3d89c93641649ef6bef706679dc69c9419185bf7df955006650c13
  payload 9844e95c6935ca9488c049123bf22fbdc27aaa114208ca519d8d374cfd7e8ccb
~~~

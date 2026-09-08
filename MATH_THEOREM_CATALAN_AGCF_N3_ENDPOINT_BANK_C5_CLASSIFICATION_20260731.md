# At parameter three, every viable endpoint bank is a pointed five-cycle

Date: 2026-07-31  
Status: complete finite classification, independently replayed.  It refutes
the canonical-Dyck endpoint recursion and identifies the first nontrivial
path-dependent Catalan transversal.  No all-parameter classification is
claimed.

## 0. Result

An endpoint bank of an AGCF on `[6]` consists of the five unordered
complement pairs formed by the endpoints of its five paths.  There are
exactly `72` viable banks.  They admit the following intrinsic description.

> Choose a distinguished coordinate `h`.  From every complement pair choose
> the endpoint containing `h` and delete `h`.  The five resulting 2-subsets
> of `[6]\{h}` are exactly the edges of a 5-cycle.

Conversely every such pointed 5-cycle bank supports an AGCF, in fact exactly
`22` AGCFs.  Hence the `72=6*(5-1)!/2` banks form one `S_6` orbit.  A bank
stabilizer has order ten and element-order histogram

\[
                       1^1,\ 2^5,\ 5^4,               \tag{0.1}
\]

so it is the natural dihedral `D_10` stabilizer of the cycle.

The canonical Dyck bank is not in this orbit and supports no AGCF.  Thus a
literal induction which freezes the `10 D_n` endpoint pairs and reuses the
canonical MSW residual is impossible already at `n=3`.

## 1. Exhaustive proof

There are ten unordered complementary pairs of triples on `[6]`.  From one
fixed endpoint of a pair there are `3!*3!=36` complement geodesics, so the
complete unoriented catalogue has

\[
                           10\cdot36=360              \tag{1.1}
\]

paths.  Each path is represented by its four middle vertices, three lower
turns, and three upper turns.  Algorithm X exact-covers the

\[
               20+15+15=50                           \tag{1.2}
\]

resources by five such rows.

The independent census visits `6,481` search nodes and returns:

\[
       1,584\text{ AGCFs},\qquad72\text{ endpoint banks},
       \qquad22\text{ AGCFs per bank}.                \tag{1.3}
\]

For each bank and each possible `h`, orient every pair toward the endpoint
containing `h` and delete `h`.  Exactly one `h` gives five distinct edges,
all degree two and connected; hence a labelled 5-cycle.  Each coordinate is
the distinguished point of exactly twelve banks.  Applying all `720`
coordinate permutations to one bank gives precisely the same set of 72;
the stabilizer computation gives (0.1).  This proves the classification.

Replay with

```text
python3 scratch/audit_catalan_agcf_n3_endpoint_bank_cycle_classification_20260731.py
```

The stronger canonical-bank no-go has a separate 180-row exact-cover replay:

```text
python3 scratch/audit_catalan_agcf_n3_canonical_dyck_endpoint_nogo_20260731.py
```

It closes UNSAT in 51 search nodes after restricting every path to start at
one of the five ordinary Dyck roots `7,11,13,19,21`.

## 2. The recursive witness lies in the classified orbit

The authenticated recursive `n=3` AGCF has endpoint pairs

\[
 (13,50),(19,44),(21,42),(25,38),(26,37).             \tag{2.1}
\]

Its distinguished coordinate is `h=3`.  Choosing the endpoint containing
`3` and deleting `3` gives

\[
       02,\ 04,\ 14,\ 15,\ 25,                      \tag{2.2}
\]

the cycle `0-2-5-1-4-0`.  Thus the explicit `2 -> 3` three-sector recursion
does not accidentally evade the classification; it produces exactly the
unique viable endpoint-bank species.

## 3. Correct replacement for canonical Dyck endpoints

The finite theorem points to a **path-dependent Catalan transversal**, not a
fixed ballot transversal.  At each recursion step the inherited endpoint
pairs and the ternary residual endpoint pairs must be chosen together.  The
bank itself is part of the inductive state:

\[
 B_{n+1}=\operatorname{child}(B_n)\ \dot\cup\
                    \operatorname{residual}(B_n).     \tag{3.1}
\]

At `n=3`, (3.1) is forced up to relabelling and is represented by the pointed
5-cycle.  At higher `n`, the current recursive `n=4` bank does not reduce to
a naive union of wreaths after deleting one distinguished point; the next
analogue must retain more than a single fixed Dyck/ballot label.  The exact
three-sector endpoint bank, rather than the canonical MSW bank, is therefore
the correct inductive object.

## 4. Reproducibility ledger

The frozen replay files have SHA-256 values

```text
efa744ef43f4b84006f86710d386a1d970f95226820f09f50b8ab2cddce5012a  scratch/audit_catalan_agcf_n3_endpoint_bank_cycle_classification_20260731.py
c4ea0ec10447faa52d574909ad3247b46e3139be35ed976a6578bbb75bfab8e7  scratch/catalan_agcf_n3_endpoint_bank_cycle_classification_20260731.audit.json
9851ffd99b8cfc396ad11cd9e5ffca4095518922ffb889b1c076d3dcf3f14c67  scratch/audit_catalan_agcf_n3_canonical_dyck_endpoint_nogo_20260731.py
930d344c52b2ec895e553b7385b9e0ebea85d86aa8b82306ffd33c51c88a0a14  scratch/catalan_agcf_n3_canonical_dyck_endpoint_nogo_20260731.audit.json
```

The canonical payload hashes written by the two independent replays are,
respectively,

```text
3e27b75daa0a0bf8868a6979c338dd552b595a349166f5451e6a7474db968fce
af9c96abac5a23b8b418a180eb50d134fe5e540ed1cd245383e2d5611bc84576
```
